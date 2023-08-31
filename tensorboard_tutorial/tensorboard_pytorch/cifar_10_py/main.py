from torch.utils.tensorboard import SummaryWriter
from dataloader import trainloader, matplotlib_imshow
import torchvision
from model import net

# default `log_dir` is "runs" - we'll be more specific here
writer = SummaryWriter('runs/fashion_mnist_experiment_1')

# get some random training images
dataiter = iter(trainloader)
images, labels = next(dataiter)

# create grid of images
img_grid = torchvision.utils.make_grid(images)

# show images
matplotlib_imshow(img_grid, one_channel=True)

# write to tensorboard
writer.add_image('four_fashion_mnist_images', img_grid)

# 可视化模型
writer.add_graph(net, images)
writer.close()
