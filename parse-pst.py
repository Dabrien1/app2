from aspose.email import PersonalStorage

# Load PST file
personalStorage = PersonalStorage.from_file("PDM.pst")

# Get folders' collection
folderInfoCollection = personalStorage.root_folder.get_sub_folders()

# Extract folders' information
for folderInfo in folderInfoCollection:
	print("Folder: " + folderInfo.display_name)
	print("Total Items: " + str(folderInfo.content_count))
	print("Total Unread Items: " + str(folderInfo.content_unread_count))