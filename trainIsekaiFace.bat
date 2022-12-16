@REM Pretrain the DualGAN model to VToonify-d pretrain.pt
@REM call "%UAI_PATH%\python.exe" -m torch.distributed.launch --nproc_per_node=1 --master_port=8765 train_vtoonify_d.py --iter 30000 --stylegan_path ./checkpoint/isekai/generator.pt --exstyle_path ./checkpoint/isekai/refined_exstyle_code.npy --batch 1 --name vtoonify_d_isekai --pretrain

@REM Train the newly pretrained.pt
call "%UAI_PATH%\python.exe" -m torch.distributed.launch --nproc_per_node=1 --master_port=8765 train_vtoonify_d.py --iter 2000 --stylegan_path ./checkpoint/isekai/generator.pt --exstyle_path ./checkpoint/isekai/refined_exstyle_code.npy --batch 2 --name vtoonify_d_isekai
