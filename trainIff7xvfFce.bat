@REM Pretrain the DualGAN model to VToonify-d pretrain.pt
@REM call "%UAI_PATH%\python.exe" -m torch.distributed.launch --nproc_per_node=1 --master_port=8765 train_vtoonify_d.py --iter 30000 --stylegan_path ./checkpoint/ff7xv/generator-001140.pt --exstyle_path ./checkpoint/ff7xv/refined_exstyle_code.npy --batch 1 --name vtoonify_d_ff7xv --pretrain

@REM Train the newly pretrained.pt
@REM call "%UAI_PATH%\python.exe" -m torch.distributed.launch --nproc_per_node=1 --master_port=8765 train_vtoonify_d.py --iter 2000 --stylegan_path ./checkpoint/ff7xv/generator-001140.pt --exstyle_path ./checkpoint/ff7xv/refined_exstyle_code.npy --batch 2 --name vtoonify_d_ff7xv

@REM Train to the 66th style
@REM call "%UAI_PATH%\python.exe"  -m torch.distributed.launch --nproc_per_node=1 --master_port=8765 train_vtoonify_d.py --iter 2000 --stylegan_path ./checkpoint/ff7xv/generator-001140.pt --exstyle_path ./checkpoint/ff7xv/refined_exstyle_code.npy --batch 2 --name vtoonify_d_ff7xv --fix_color --fix_degree --style_degree 0.5 --fix_style --style_id 66