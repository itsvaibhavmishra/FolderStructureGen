# Folder Structure Generator by [Vaibhaw Mishra](https://github.com/itsvaibhavmishra)

> Please leave a ⭐Star if this repo was helpful

FolderStructureGen is a tool designed to generate folder structures for your codebase. You can exclude specific folders or files by adding them to the exclusion field. Choose between the CLI version or GUI version.

- To run the CLI script, refer to the README.md inside the CLI_Folder_Generator directory.
- To run the GUI script, refer to the README.md inside the GUI_Folder_Generator directory.

## ⚜️ How to Use?

- Start the generator by opening the `GUIStructureGen.exe` file and wait for a window to pop up.
- Either type the full path for your folder in the `Select Folder` field or click on `Open` to select the folder using a file dialog.
- If needed, add files/folders to exclude inside the `Excluded items` field. Separate multiple entries with commas, and for files, include their respective extensions (e.g., `.py`, `.txt`, `.md`, etc.).
- Click on `Generate` to create your folder structure in seconds.
- Click on the `Reset` button to clear the fields and start over.
- Click on the `Readme` button to access the README.md on GitHub.
- Your folder structure will be generated inside the folder you selected.

## 🤖 Generate an Executable Version for GUI_Generator

While inside the `FolderStructureGen/` folder, run the following command:

```bash
pip install pyinstaller && pyinstaller GUIStructureGen.spec
```

Now look for the `GUIStructureGen.exe` file inside the dist/ folder.

## 🪜 Folder Structure

```
FolderStructureGen/
├── CLI_Folder_Generator/
│   ├── README.md
│   ├── structureGen.py
├── GUI_Folder_Generator/
│   ├── GUIStructureGen.py
│   ├── README.md
├── .gitignore
├── GUIStructureGen.spec
├── LICENSE
├── README.md
```

<br/>

<div align="center">
<img src="https://komarev.com/ghpvc/?username=itsvaibhavmishra&&style=for-the-badge" align="center" />
</div>

<br/>
