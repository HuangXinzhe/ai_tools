import wandb

wandb.login()

#初始化wandb
run = wandb.init(
    # Set the project where this run will be logged
    project = "test_task",
    group = "keywords",
    notes="tf-idf在top-20上sum最多的5个关键词",
    name="tf-idf_top-20_5",
    config={
        "learning_rate": 0.01
    })