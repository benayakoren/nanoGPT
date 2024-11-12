# evaluate the base gpt2
# n_blocks=24, n_head=16, emb_dim=1024
# 350M parameters
batch_size = 8
eval_iters = 500 # use more iterations to get good estimate
eval_only = True
wandb_log = False
init_from = 'gpt2-medium'
