# evaluate the base gpt2
# n_blocks=48, n_head=25, emb_dim=1600
# 1558M parameters
batch_size = 8
eval_iters = 500 # use more iterations to get good estimate
eval_only = True
wandb_log = False
init_from = 'gpt2-xl'
