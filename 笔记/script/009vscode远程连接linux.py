# 1.安装插件： remote-ssh
# 2.点机左下角连接新建ssh的配置
#     Host vs119
#       HostName 172.18.128.119
#       User root
#       Port 22
# 3.win下生成公私密钥：cmd里面输入 ssh-keygen，连续3个回车。在c:/lyj157175/.ssh下生成：id_rsa(私钥)和id_rsa.pub(公钥)
# 找到linux下的root下的.ssh文件夹，将id_rsa.pub(公钥)的内容定向到authorized_keys文件下即可
#
# 4.vscode无需密码连接linux服务器