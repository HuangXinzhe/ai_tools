from torch.utils.tensorboard import SummaryWriter
import numpy as np

writer = SummaryWriter('runs/keywords_experiment')
# 创建numpy数组
keywords_data = np.array([100, 40, 50, 20, 3, 60, 9, 8, 70, 10])

for n_iter in range(10):
    writer.add_scalar('Loss/test', keywords_data[n_iter], n_iter)

writer.close()