# FSUtils-doc

### get_recur_file_list

```python
get_recur_file_list(root, ignore_keywords=None)
```

- **Parameters**

  - **root (str)**

    The path yout want to recur all directories and files .

  - **ignore_keywords (list[ str])**

    The keywords you want to ignore in the paths.

- **Returns**

  - **all_dirs_list (list[ str])**

    All direcitories under `root` path.

  - **all_files_list (list[ str])**

    All files under `root` path.

### split_files

```python
split_files(root_files_dir, output_dir, num_per_group, shuffle=False)
```

- **Parameters**

  - **root_files_dir (str)** 

    The root directory which contains all files you want to split.

  - **output_dir (str)**

    The output directory which contains all results after split. Index 1, 2, ... will be the subfolders of `output_dir`.

  - **num_per_group (int)**

    The number of each group after split.

  - **shuffle (boolean)**

    Will the result be shuffled or not.

- **Returns**

  - **None**

    The results will be stored in `output_dir`.
