## Folder Structure Generator (GUI)

> Please leave a ⭐Star if this repo was helpful

This script provides a graphical user interface (GUI) for generating folder structures for specified directories. You can customize the folder structure by excluding certain folders or files.

## Usage

1. **Start the Script:**

   - Open your terminal or command prompt.
   - Navigate to the directory containing `GUIStructureGen.py`.
   - Run the script using the following command:

   ```bash
   $ python GUIStructureGen.py
   ```

2. **Generate Folder Structure:**

   - Upon running the script, a GUI window will appear.
   - You can either manually type the full path of the folder or click on `Open` to select the folder using a file dialog.
   - If needed, add files/folders to exclude inside the `Excluded items` field. Each file/folder should be separated by a comma, and for files, make sure to include their respective extensions (e.g., `.py`, `.txt`, `.md`, etc.).
   - Click on `Generate` to start the generation process.

3. **View Generated Structure:**

   - Once the generation process is complete, the folder structure will be generated inside the folder you selected.
   - The structure will be saved as a Markdown (.md) file named <folder_name>\_structure.md.

4. **Generate spec & exe**

   - While inside `GUI_Folder_Generator`, generate `build`, `dist`, and `GUIStructureGen.py` using the following command:

   ```bash
   pip install pyinstaller && pyinstaller --onefile GUIStructureGen.py
   ```

## Example

Suppose you want to generate a folder structure for a directory named `project`, excluding the `docs` folder and `demo.txt` file. Here's how you would use the GUI:

- Click on `Open` and select the `project` folder.
- In the `Excluded items` field, enter `docs, demo.txt`.
- Click on `Generate` to start the generation process.

After execution, the generated structure will be saved as `project_structure.md` within the `project` folder.

<br/>

<div align="center">
<img src="https://komarev.com/ghpvc/?username=itsvaibhavmishra&&style=for-the-badge" align="center" />
</div>

<br/>
