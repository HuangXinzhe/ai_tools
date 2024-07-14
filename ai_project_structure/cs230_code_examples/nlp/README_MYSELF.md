# 构建项目详细步骤
1. 下载数据集
2. 构建数据集
根据实际情况，有的数据集下载有之后不需要特殊处理
```
python build_kaggle_dataset.py
```
3. 构建词汇表
目前大模型项目不需要构建词汇表了
```
python build_vocab.py --data_dir  data/small
# 或
python build_vocab.py --data_dir data/kaggle
```

## 代码结构
```
data/
    train/
    dev/
    test/
experiments/
model/
    *.py
build_dataset.py
train.py
search_hyperparams.py
synthesize_results.py
evaluate.py
```
- data/：将包含项目的所有数据（通常不存储在 GitHub 上），并具有显式的 train/dev/test 拆分
- experiments：包含不同的实验（将在下一节中解释）
- model/：定义训练或评估中使用的模型和函数的模块。我们的 PyTorch 和 TensorFlow 示例不同
- build_dataset.py：创建或转换数据集，将拆分为 train/dev/test
- train.py：根据输入数据训练模型，并评估开发集上的每个纪元
- search_hyperparams.py：使用不同的超参数多次运行train.py
- synthesize_results.py：在目录中浏览不同的实验，并显示一个漂亮的结果表
- evaluate.py：在测试集上评估模型（应在项目结束时运行一次）

## 快速开始
### 运行实验
```
python train.py --model_dir experiments/base_model
```
- 实验结束后结果
```
experiments/
    base_model/
        params.json
        ...
    learning_rate/
        lr_0.1/
            params.json
        lr_0.01/
            params.json
    batch_norm/
        params.json
```
训练后的每个目录将包含多个内容：
- params.json：超参数列表，JSON格式
- train.log：训练日志（我们打印到控制台的所有内容）
- train_summaries：TensorBoard 的训练摘要（仅限 TensorFlow）
- eval_summaries：TensorBoard 的评估摘要（仅限 TensorFlow）
- last_weights：从最后 5 个纪元中保存的权重
- best_weights：最佳权重（基于开发精度）
### 评估实验
```
python evaluate.py --model_dir experiments/base_model
```
### 超参数搜索
```
experiments/
    learning_rate/
        params.json



python search_hyperparams.py --parent_dir experiments/learning_rate



experiments/
    learning_rate/
        learning_rate_0.001/
            metrics_eval_best_weights.json
        learning_rate_0.01/
            metrics_eval_best_weights.json
        ...
```
### 显示多个结果
```
python synthesize_results.py --parent_dir experiments/learning_rate
```
