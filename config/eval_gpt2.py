# evaluate the base gpt2
# n_blocks=12, n_head=12, emb_dim=768
# 124M parameters
batch_size = 8
eval_iters = 500 # use more iterations to get good estimate
eval_only = True
wandb_log = False
init_from = 'gpt2'
