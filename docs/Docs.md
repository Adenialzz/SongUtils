# Docs

## FSUtils

### [Method] get_recur_file_list

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

### [Method] split_files

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

- **Returns** None

  - The results will be stored in `output_dir`.

## MetricUtils

### [Class] AverageMeter

```python
class AverageMeter(object)
```

> Description: An utilitiy for tracking metric updates.

#### methods

- **reset**

  ```python
  reset(self)
  ```

  >Description: Set all values as 0.

  - **Parameters** None
  - **Returns** None

- **uodate**

  ```python
  update(self, val, n=1)
  ```

  > Description: Update Values.

  - **Parameters**

    - **val (float)** 

      The value to update.

    - **n (int)**

      The number of samples used to update the `val`.

#### usage example

```python
_loss = AverageMeteric()
for epoch_step, data in enumerate(loader):
    # ...
    loss = self.loss_func(output, label)
    _loss.update(loss.item())
		writer.add_scalar("loss", _loss.avg, epoch_step)
```

### [Mehod] accuracy

```python
accuracy(output, target, topk=(1, ))
```



>Descrition: Get tokp accuaracy of classificiation.

- **Parameters**

  - **output (tensor)**

    The output of model.

  - **target  (tensor)**

    The label in dataset.

  - **topk (list / tuple)**

    List / tuple of K values.

- **Returns**

  - **res [list]**

    Top K accuracy.