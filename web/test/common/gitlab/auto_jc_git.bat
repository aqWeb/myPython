set yr_git=localhost/xxx/xxx.git
set model=xxx
set branch=release/2.1.1
set xx_git=localhost/xxx/xxx.git
set base_dir=E:/local/xxx
set local_model_path=/lang









E:
cd %base_dir%%local_model_path%
git clone %yr_git%
cd %model%
git checkout %branch%
git remote add origin %xx_git%
git remote rm origin
git remote add origin %xx_git%
git push -u origin %branch%