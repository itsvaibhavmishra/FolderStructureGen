## Folder Structure Generator (CLI)

> Please leave a ⭐Star if this repo was helpful

This script allows you to generate a folder structure for a specified directory. You can customize the folder structure by excluding certain folders or files.

## Usage

1. **Download the Script:**

   - Place `structureGen.py` inside the root folder of your project.

2. **Run the Script:**

   - Open your terminal or command prompt.
   - Navigate to the directory containing `structureGen.py`.
   - Run the script using the following command:

   ```bash
   $ python structureGen.py
   ```

3. **Generate Folder Structure:**

   - Upon running the script, you will be prompted to enter the name of the folder for which you want to generate the folder structure.
   - If you want to crawl the current folder, simply type ".".
   - Next, you can specify any folders or files you wish to exclude from the structure. Separate multiple entries with commas and include filenames with extensions (e.g., `.txt`, `.md`, etc.).
   - Press Enter to start the generation process.

4. **View Generated Structure:**
   - Once the script completes execution, the folder structure will be generated inside the selected folder.
   - The structure will be saved as a Markdown (.md) file named `<folder_name>_structure.md`.

## Example

Suppose you want to generate a folder structure for a directory named `project`, excluding the `docs` folder and any `.txt` files. Here's how you would run the script:

```bash
$ python structureGen.py
Enter name of the folder to generate structure: project
Enter folders or files to exclude (comma-separated): docs, .txt
```

After execution, the generated structure will be saved as `project_structure.md` within the `project` folder.

<br/>

<div align="center">
<img src="https://komarev.com/ghpvc/?username=itsvaibhavmishra&&style=for-the-badge" align="center" />
</div>

<br/>
