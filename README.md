# 概要
ロボットシステム学　課題２　です。

上田先生の授業で扱ったコードに100times.pyを追加しました。

下のリンクが授業のスライド資料のURLです。

https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/24

# 動作環境

・Raspberry Pi4 Model BはノートPC（Windows10)を経由してインターネット接続してます。

（Raspberry Pi4を今後ラズパイと略すことがあります）

・WSL2のubunu20.04.3 LTSを使用してます。

　また、ラズパイもubunu20.04.3 LTSです。

・ROSのインストールは上田先生のros_setup_scripts_ubuntu20.04_serverを参考にしました。

なお、rosのパラメータは以下の通りです。

    ros distro: noetic
    ros version : 1.15.13


・ノートPCを経由してインターネット接続する方法のリンク

　https://twitter.com/ryuichiueda/status/1178124814076149761


・ラズパイにubuntuをインストールする方法のリンク

　https://twitter.com/ryuichiueda/status/1250644188992962560

・ubuntu20.04にrosをインストールする方法のリンク

 https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server


# 使用した物
・Raspberry Pi4 Model B　× 1

・マイクロSDカード（ラズパイ用） × 1

・ラズパイ用の電源（端子はtype-c) × 1

・ノートPC（Windows10 / 64bit) × 1

・wifi環境（私は2.4GHzで通信）

# 下準備
    $cd
    $mkdir -p catkin_ws/src
    $cd ~/catkin_ws/src
    $catkin_init_workspace
  これでsrcにCMakeList.txtが作成されたはずです。
    `$ls`  で確認してください。
   
    $vi ~/.bashrc
コードの下の方（118行付近）にsource ~exportと始まるところがあります。   
そこに

    source /opt/ros/noetic/setup.bash
    source ~/catkin_ws/devel/setup.bash
    export ROS_MASTER_URI=http://localhost:11311
    export ROS_HOSTNAME=localhost
    
 があるように修正してください。

(私のときは source ~/catkin_ws/devel/setup.bash のみ追加しました。）
その後、

    $cd /catkin_ws
    $catkin_make
    $source ~/.bashrc
    
 でビルドします。確認として、
 
     $ echo $ROS_PACKAGE_PATH
     /home/ubuntu/catkin_ws/src:/opt/ros/noetic/share
 
catkin_ws/srcがあることを確認してください。

ワークスペースにリポジトリをコピーし、ノードがあるか確認します。

    $cd ~/catkin_ws/src
    $git clone git@github.com:2daimehorisota/ros-test.git
    $cd  ~/catkin_ws/src/ros-test/mypkg/scripts
    $ls
で中に
    `100times.py count.py twice.py` があることを確認してください。
    
 最後にWSLで端末を４つ以上立ち上げ、全てラズパイにログインします。
 
これで下準備は完了です。
   
# count.pyの実行

端末１で

    $roscore

を実行します。

次に端末２で

    $cd  ~/catkin_ws/src/ros-test/mypkg/scripts
    $chmod +x count.py
    $rosrun mypkg count.py

を実行します。

端末３で

    $rostopic echo /count_up
 
 を実行すると、端末３で1刻みでカウントされる様子が確認できます。

twice.pyと100times.pyを実行する際は端末３を停止させる`[ctrl] + [c]`,

もしくは１つ端末を増やすようにお願いします。 

# twice.pyの実行
count.pyの出力メッセージを用いるため、count.pyを実行した上でtwice.pyを実行させます。

（端末１と端末２は停止させません）

端末４で

    $cd  ~/catkin_ws/src/ros-test/mypkg/scripts
    $chmod +x twice.py
    $rosrun mypkg twice.py

を実行させます。

端末３を停止しているのなら、端末３で

    $rostopic echo /twice
    
を実行すれば、２刻みでカウントされる様子が確認できます。

もし、端末３を止めない場合は新しく追加した端末でラズパイにログインをして上のコマンドを実行すれば同じようにカウントされるのを確認できます。

# 100times.pyの実行
count.pyの出力メッセージを用いるため、count.pyを実行した上で100times.pyを実行させます。

twice.pyと同時に動かせますが、本説明ではtwice.pyは停止させています。

（端末１と端末２は停止させません）

端末４で

    $cd  ~/catkin_ws/src/ros-test/mypkg/scripts
    $chmod +x 100times.py
    $rosrun mypkg 100times.py
を実行します。

端末３を停止しているのなら、端末３で

    $rostopic echo /100times
    
を実行すれば、100刻みでカウントされる様子が確認できます。

もし、端末３を止めない場合は新しく追加した端末でラズパイにログインをして上のコマンドを実行すれば同じようにカウントされるのを確認できます。

# 停止方法

停止させたい場合はそれぞれの端末で`[ctrl] + [c]`を実行すれば停止します。

# 実際の動作の様子

実際に動く様子を動画にしています。
YouTubeのリンク
https://www.youtube.com/watch?v=MVgvhaMdmvE


# ライセンス
BSD 3-Clause "New" or "Revised" License

https://github.com/2daimehorisota/ros-test/blob/42a2daed710f48c0962ef54d8da02f072265ff48/LICENSE
