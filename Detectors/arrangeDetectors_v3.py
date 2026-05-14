import os
from sys import argv, exit
from datetime import datetime
from json import load as loadJSON
try:
	from yaml import dump as dumpYAML
except:
	print("Cannot import ``dump`` from ``yaml``. Please try to install ``yaml`` via ``python -m pip install PyYAML``. ")
	print("Please press the enter key to exit. ")
	try:
		input()
	except:
		print()
	exit(-1)
try:
	os.chdir(os.path.abspath(os.path.dirname(__file__)))
except:
	pass
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EOF = (-1)


class Detectors:
	def __init__(self:object) -> object:
		self.__data = None
		self.__introduction = None
		self.__flag = False
	def load(self:object, jsonFilePath:str, encoding:str = "utf-8") -> bool:
		try:
			with open(jsonFilePath, "r", encoding = encoding) as f:
				j = loadJSON(f)
			self.__data = []
			if "$C$" in j:
				self.__data.extend(j["$C$"])
			if "$D$" in j:
				self.__data.extend(j["$D$"])
			self.__introduction = j["Introduction"] if "Introduction" in j else {"*":""}
			self.__flag = True
			return True
		except BaseException as e:
			print("Cannot load data from \"{0}\". Details are as follows. \n\t{1}".format(jsonFilePath, e))
			return False
	def checkDetectorFolderPath(self:object, detectorFolderPath:str = ".") -> int:
		if self.__flag and isinstance(detectorFolderPath, str) and os.path.isdir(detectorFolderPath):
			issueCnt, fileNames = 0, []
			for item in os.listdir(detectorFolderPath):
				if os.path.splitext(item)[0] != "README" and os.path.splitext(item)[0] != "TABLE" and os.path.splitext(item)[1] not in (".old", ".py"):
					fileNames.append(item)
			for obj in self.__data:
				if "category" in obj and len(obj["category"]) <= 5 and obj["category"].startswith("$D") and obj["category"].endswith("$"):
					if "name" in obj and "latestVersion" in obj:
						fileNameA = "{0}_{1}.apk".format(obj["name"], obj["latestVersion"])
						fileNameB = fileNameA + "s"
						fileNameC, fileNameD = fileNameA + ".nomedia", fileNameB + ".nomedia"
						if fileNameA in fileNames:
							fileNames.remove(fileNameA)
						elif fileNameB in fileNames:
							fileNames.remove(fileNameB)
						elif fileNameC in fileNames:
							fileNames.remove(fileNameC)
						elif fileNameD in fileNames:
							fileNames.remove(fileNameD)
						else:
							issueCnt += 1
							print("File \"{0}\" or File \"{1}\" is not in Folder \"{2}\". ".format(fileNameA, fileNameB, detectorFolderPath))
					else:
						issueCnt += 1
						print("An invalid record {0} is found. ".format(obj))
					if "image" in obj:
						for imageName in obj["image"].values():
							if imageName in fileNames:
								fileNames.remove(imageName)
							else:
								issueCnt += 1
								print("Image \"{0}\" is not in Folder \"{1}\". ".format(imageName, detectorFolderPath))
			if fileNames:
				issueCnt += len(fileNames)
				print("Extra files {0} are detected. ".format(fileNames) if len(fileNames) > 1 else "An extra file entitled \"{0}\" is detected. ".format(fileNames[0]))
			return issueCnt
		else:
			return -1
	def __getSourceStatus(self:object, booleanValue:bool, language:str) -> str:
		if isinstance(booleanValue, bool) and isinstance(language, str):
			if booleanValue:
				return {"zh-CN":"是"}.get(language, "Yes")
			else:
				return {"zh-CN":"否"}.get(language, "No")
		else:
			return ""
	def __getCategory(self:object, code:str, language:str) -> str:
		if isinstance(code, str) and isinstance(language, str):
			d = {
				"$C_A$":{"*":"Abroad Android Desktop Application", "zh-CN":"境外安卓桌面应用"}, "$C_K$":{"*":"North Korea Android Desktop Application", "zh-CN":"朝鲜安卓桌面应用"}, 
				"$C_L$":{"*":"Local Android Desktop Application", "zh-CN":"本地安卓桌面应用"}, "$C_M$":{"*":"Mainland China Android Desktop Application", "zh-CN":"中国大陆安卓桌面应用"}, 
				"$D_A$":{"*":"Apatch Detection", "zh-CN":"Apatch 检测"}, "$D_E$":{"*":"Environment Detection", "zh-CN":"环境检测"}, "$D_F$":{"*":"Flag Detection", "zh-CN":"安全标志检测"}, 
				"$D_I$":{"*":"Information Gathering", "zh-CN":"信息收集"}, "$D_K$":{"*":"Key Attestation", "zh-CN":"密钥认证"}, "$D_L$":{"*":"Applist Detection", "zh-CN":"应用列表检测"}, 
				"$D_M$":{"*":"Magisk Detection", "zh-CN":"面具检测"}, "$D_P$":{"*":"Play Integrity Check", "zh-CN":"Play 完整性检测"}, 
				"$D_S$":{"*": "SELinux Policy Detection", "zh-CN": "SE 策略检测"}
			}
			if code in d:
				return d[code][language] if language in d[code] else d[code]["*"]
			else:
				print("The code \'{0}\' has no meanings in developing purpose statements. ".format(code))
				return ""
		else:
			return ""
	def __getReleaseDate(self:object, code:str, language:str) -> str:
		if isinstance(code, str) and isinstance(language, str):
			if len(code) >= 8 and code[-8:].isdigit():
				d = {
					"":"", "=":"", "==":"", "<":{"*":"Before", "zh-CN":"早于"}, "<=":{"*":"On or Before", "zh-CN":"不晚于"}, 
					">":{"*":"After", "zh-CN":"晚于"}, ">=":{"*":"On or After", "zh-CN":"不早于"}, "!=":{"*":"Not On", "zh-CN":"不是"}
				}
				symbol = code[:-8].strip()
				if symbol in d:
					year, month, day = int(code[-8:-4]), int(code[-4:-2]), int(code[-2:])
					try:
						date = datetime(year, month, day)
					except:
						print("The date in the code \"{0}\" is invalid in release date statements. ".format(code))
						return ""
					if "zh-CN" == language:
						return "{0} {1} 年 {2} 月 {3} 日".format(d[symbol]["zh-CN"] if isinstance(d[symbol], dict) else d[symbol], year, month, day)
					else:
						months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
						suffix = "th" if day % 100 in (11, 12, 13) else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
						return "{0} {1} {2}{3}, {4}".format(d[symbol]["*"] if isinstance(d[symbol], dict) else d[symbol], months[month - 1], day, suffix, year)
				else:
					print("The symbol in the code \"{0}\" has no meanings in release date statements. ".format(code))
			else:
				print("The code \"{0}\" has no meanings in release date statements. ".format(code))
		return ""
	def __convertToMarkdownTable(self:object, language:str) -> str:
		if self.__flag and isinstance(language, str):
			if "zh-CN" == language:
				markdown = "## 检测软件\n\n| 名称 | 应用包名 | 官方链接 | 开源 | 类别 | 最新版本 | 发行日期 |\n| - | - | - | - | - | - | - |\n"
				separator = "；"
			elif len(language) == 2 and "A" <= language[0] <= "Z" and "A" <= language[1] <= "Z":
				markdown = "## Detectors\n\n| Name | Package Name(s) | Official Link(s) | Open-source | Category | Latest Version | Release Date |\n| - | - | - | - | - | - | - |\n"
				separator = "; "
			else:
				return language
			for detector in self.__data:
				markdown += "| "
				markdown += detector["name"] + " | " if "name" in detector else "| "
				markdown += (separator.join(["``{0}``".format(pkg) for pkg in detector["packageName"]]) if isinstance(
					detector["packageName"], list
				) else "``{0}``".format(detector["packageName"])) + " | " if "packageName" in detector else "| "
				markdown += (separator.join(["[{0}]({0})".format(link) for link in detector["officialLink"]]) if isinstance(
					detector["officialLink"], list
				) else "[{0}]({0})".format(detector["officialLink"])) + " | " if "officialLink" in detector else "| "
				markdown += self.__getSourceStatus(detector["openSource"], language) + " | " if "openSource" in detector else "| "
				markdown += self.__getCategory(detector["category"], language) + " | " if "category" in detector else "| "
				markdown += "``{0}`` | ".format(detector["latestVersion"]) if "latestVersion" in detector else "| "
				markdown += self.__getReleaseDate(detector["releaseDate"], language) + " |\n" if "releaseDate" in detector else "|\n"
			return markdown
		else:
			return ""
	def __convertToMarkdownText(self:object, language:str) -> str:
		if self.__flag and isinstance(language, str):
			if "en" == language:
				txt = "## Detectors\n\n{0}\n\n".format(self.__introduction.get(language, self.__introduction["*"]))
				for detector in self.__data:
					txt += "### " + detector["name"] + "\n\n"
					if "alias" in detector and ("*" in detector["alias"] or "en" in detector["alias"]):
						txt += "- **Alias**: "
						aliasVector = []
						if "*" in detector["alias"]:
							aliasVector += detector["alias"]["*"] if isinstance(detector["alias"]["*"], (tuple, list)) else [detector["alias"]["*"]]
						if "en" in detector["alias"]:
							aliasVector += detector["alias"]["en"] if isinstance(detector["alias"]["en"], (tuple, list)) else [detector["alias"]["en"]]
						txt += "; ".join(aliasVector) + "\n"
					if "packageName" in detector:
						if isinstance(detector["packageName"], list):
							txt += "- **Package Names**: " + "; ".join(["``{0}``".format(pkg) for pkg in detector["packageName"]]) + "\n"
						else:
							txt += "- **Package Name**: " + "``{0}``".format(detector["packageName"]) + "\n"
					if "officialLink" in detector:
						if isinstance(detector["officialLink"], list):
							txt += "- **Official Links**: " + "; ".join(["[{0}]({0})".format(link) for link in detector["officialLink"]]) + "\n"
						else:
							txt += "- **Official Link**: " + detector["officialLink"] + "\n"
					txt += "- **Source Status**: " + self.__getSourceStatus(detector["openSource"], "en") + "\n" if "openSource" in detector else ""
					txt += "- **Category**: " + self.__getCategory(detector["category"], "en") + "\n" if "category" in detector else ""
					txt += "- **Latest Version**: ``{0}``\n".format(detector["latestVersion"]) if "latestVersion" in detector else ""
					txt += "- **Release Date**: " + self.__getReleaseDate(detector["releaseDate"], "en") + "\n" if "releaseDate" in detector else ""
					if "detectionRemark" in detector and ("*" in detector["detectionRemark"] or "en" in detector["detectionRemark"]):
						txt += "- **Detection Remark**: "
						if "*" in detector["detectionRemark"]:
							txt += detector["detectionRemark"]["*"]
						if "en" in detector["detectionRemark"]:
							txt += detector["detectionRemark"]["en"]
						txt += "\n"
					if "image" in detector and "*" in detector["image"]:
						txt += "- ![{0}]({0})\n".format(detector["image"]["*"])
					if "image" in detector and "en" in detector["image"]:
						txt += "- ![{0}]({0})\n".format(detector["image"]["en"])
					txt += "\n"
				return txt
			elif "zh-CN" == language:
				txt = "## 检测软件\n\n{0}\n\n".format(self.__introduction.get(language, self.__introduction["*"]))
				for detector in self.__data:
					txt += "### " + detector["name"] + "\n\n"
					if "alias" in detector and ("*" in detector["alias"] or "zh-CN" in detector["alias"]):
						txt += "- **应用别称**："
						aliasVector = []
						if "*" in detector["alias"]:
							aliasVector += detector["alias"]["*"] if isinstance(detector["alias"]["*"], (tuple, list)) else [detector["alias"]["*"]]
						if "zh-CN" in detector["alias"]:
							aliasVector += detector["alias"]["zh-CN"] if isinstance(detector["alias"]["zh-CN"], (tuple, list)) else [detector["alias"]["zh-CN"]]
						txt += "; ".join(aliasVector) + "\n"
					if "packageName" in detector:
						if isinstance(detector["packageName"], list):
							txt += "- **应用包名**：" + "；".join(["``{0}``".format(pkg) for pkg in detector["packageName"]]) + "\n"
						else:
							txt += "- **应用包名**：" + "``{0}``".format(detector["packageName"]) + "\n"
					if "officialLink" in detector:
						if isinstance(detector["officialLink"], list):
							txt += "- **官方链接**：" + "；".join(["[{0}]({0})".format(link) for link in detector["officialLink"]]) + "\n"
						else:
							txt += "- **官方链接**：" + "[{0}]({0})".format(detector["officialLink"]) + "\n"
					txt += "- **开源状态**：" + self.__getSourceStatus(detector["openSource"], "zh-CN") + "\n" if "openSource" in detector else ""
					txt += "- **类别**：" + self.__getCategory(detector["category"], "zh-CN") + "\n" if "category" in detector else ""
					txt += "- **最新版本**：``{0}``\n".format(detector["latestVersion"]) if "latestVersion" in detector else ""
					txt += "- **发行日期**：" + self.__getReleaseDate(detector["releaseDate"], "zh-CN") + "\n" if "releaseDate" in detector else ""
					if "detectionRemark" in detector and ("*" in detector["detectionRemark"] or "zh-CN" in detector["detectionRemark"]):
						txt += "- **检测备注**："
						if "*" in detector["detectionRemark"]:
							txt += detector["detectionRemark"]["*"]
						if "zh-CN" in detector["detectionRemark"]:
							txt += detector["detectionRemark"]["zh-CN"]
						txt += "\n"
					if "image" in detector and "*" in detector["image"]:
						txt += "- ![{0}]({0})\n".format(detector["image"]["*"])
					if "image" in detector and "zh-CN" in detector["image"]:
						txt += "- ![{0}]({0})\n".format(detector["image"]["zh-CN"])
					txt += "\n"
				return txt
			elif len(language) == 2 and "A" <= language[0] <= "Z" and "A" <= language[1] <= "Z":
				txt = "## Detectors\n\n"
				for detector in self.__data:
					txt += "### " + detector["name"] + "\n\n"
					if "alias" in detector and "*" in detector["alias"]:
						txt += "- **Alias**: "
						aliasVector = []
						if "*" in detector["alias"]:
							aliasVector += detector["alias"]["*"] if isinstance(detector["alias"]["*"], (tuple, list)) else [detector["alias"]["*"]]
						txt += "; ".join(aliasVector) + "\n"
					if "packageName" in detector:
						if isinstance(detector["packageName"], list):
							txt += "- **Package Names**: " + "; ".join(["``{0}``".format(pkg) for pkg in detector["packageName"]]) + "\n"
						else:
							txt += "- **Package Name**: " + "``{0}``".format(detector["packageName"]) + "\n"
					if "officialLink" in detector:
						if isinstance(detector["officialLink"], list):
							txt += "- **Official Links**: " + "; ".join(["[{0}]({0})".format(link) for link in detector["officialLink"]]) + "\n"
						else:
							txt += "- **Official Link**: " + detector["officialLink"] + "\n"
					txt += "- **Source Status**: " + self.__getSourceStatus(detector["openSource"], "*") + "\n" if "openSource" in detector else ""
					txt += "- **Category**: " + self.__getCategory(detector["category"], "*") + "\n" if "category" in detector else ""
					txt += "- **Latest Version**: ``{0}``\n".format(detector["latestVersion"]) if "latestVersion" in detector else ""
					txt += "- **Release Date**: " + self.__getReleaseDate(detector["releaseDate"], "*") + "\n" if "releaseDate" in detector else ""
					if "detectionRemark" in detector and "*" in detector["detectionRemark"]:
						txt += "- **Detection Remark**: "
						if "*" in detector["detectionRemark"]:
							txt += detector["detectionRemark"]["*"]
						txt += "\n"
					if "image" in detector and "*" in detector["image"]:
						txt += "- ![{0}]({0})\n".format(detector["image"]["*"])
					txt += "\n"
				return txt
			else:
				return language
		else:
			return ""
	def __convertToYml(self:object) -> str:
		return dumpYAML(self.__data, allow_unicode = True, sort_keys = False, default_flow_style = False, indent = 2, width = 120) if self.__flag else ""
	def __handleFolder(self:object, fd:str) -> bool:
		try:
			folder = str(fd)
		except:
			return False
		if not folder:
			return True
		elif os.path.exists(folder):
			return os.path.isdir(folder)
		else:
			try:
				os.makedirs(folder)
				return True
			except:
				return False
	def toMarkdownFile(self:object, markdownFilePath:str = None, languages:tuple|list = ("en", "\n---\n", "zh-CN"), isTable:bool = False, encoding:str = "utf-8") -> str|bool:
		if self.__flag and isinstance(isTable, bool):
			markdown = ""
			for language in languages:
				markdown += self.__convertToMarkdownTable(language) if isTable else self.__convertToMarkdownText(language)
			if isinstance(markdownFilePath, str):
				if self.__handleFolder(os.path.split(markdownFilePath)[0]):
					try:
						with open(markdownFilePath, "w", encoding = encoding) as f:
							f.write(markdown)
						print("Successfully wrote data in the format of markdown to \"{0}\". ".format(markdownFilePath))
						return True
					except BaseException as e:
						print("Cannot write data in the format of markdown to \"{0}\". Details are as follows. \n\t{1}".format(markdownFilePath, e))
				else:
					print("Cannot write data in the format of markdown to \"{0}\" since the parent folder was not created successfully. ".format(markdownFilePath))
				return False
			else:
				return markdown
		else:
			return False
	def toYmlFile(self:object, ymlFilePath:str = None, encoding:str = "utf-8") -> str|bool:
		if self.__flag:
			yml = self.__convertToYml()
			if isinstance(ymlFilePath, str):
				if self.__handleFolder(os.path.split(ymlFilePath)[0]):
					try:
						with open(ymlFilePath, "w", encoding = encoding) as f:
							f.write(yml)
						print("Successfully wrote data in the format of YML to \"{0}\". ".format(ymlFilePath))
						return True
					except BaseException as e:
						print("Cannot write data in the format of YML to \"{0}\". Details are as follows. \n\t{1}".format(ymlFilePath, e))
				else:
					print("Cannot write data in the format of YML to \"{0}\" since the parent folder was not created successfully. ".format(ymlFilePath))
				return False
			else:
				return yml
		else:
			return False


def main() -> int:
	jsonFilePath, detectorFolderPath, markdownTextFilePath, markdownTableFilePath, ymlFilePath = "README.json", ".", "README.md", "TABLE.md", "README.yml"
	detectors = Detectors()
	bRet = detectors.load(jsonFilePath)
	detectors.checkDetectorFolderPath(detectorFolderPath = detectorFolderPath)
	if bRet:
		booleans = [
			detectors.toMarkdownFile(markdownTextFilePath, languages = ("en", "\n---\n\n", "zh-CN"), isTable = False), 
			detectors.toMarkdownFile(markdownTableFilePath, languages = ("en", "\n---\n\n", "zh-CN"), isTable = True), 
			detectors.toYmlFile(ymlFilePath)
		]
	exitCode = EXIT_SUCCESS if bRet and all(booleans) else EXIT_FAILURE
	try:
		input("Please press the enter key to exit ({0}). ".format(exitCode))
	except:
		pass
	return exitCode



if "__main__" == __name__:
	exit(main())