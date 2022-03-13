python -m torch.distributed.launch --nproc_per_node 3 train_mnist.py \
	--gpu-id 0,1,2 \
	--batchSize 10240 \

