## Folder Structure Generator by [Vaibhaw Mishra](https://github.com/itsvaibhavmishra)

As the name suggests FolderStructureGen would generate a folder structure for your codebase. You can exclude `folder/files` by adding them to exclude field.
Choose between CLI version or GUI version.

## 🤖Generate a executable version for GUI_Generator

While inside of `FolderStructureGen/` folder, run the following command:

```bash
 pyinstaller GUIStructureGen.spec
```

Now look for the `GUIStructureGen.exe` file inside of dist/ folder

## 🪜Folder Structure

```
FolderStructureGen/
├── .gitignore
├── CLI_Folder_Generator/
│   ├── structureGen.py
├── GUIStructureGen.spec
├── GUI_Folder_Generator/
│   ├── GUIStructureGen.py
├── README.md
```
