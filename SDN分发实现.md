# SDN��������ݮ���ϵ�ʵ��
## ����Ŀ��
ʵ����ͼ�ṹ��SDN������
![avatar](����ṹͼʾ.PNG)
��adhoc����Ϊ�������ڿ��ƽڵ����ݮ��������ryu��������OVS���������Լ�һ��������������������������linux�������ռ�ʵ�ֵģ������������������������ͨ�ڵ����ݮ��������OVS��������һ������������  
ͨ��ryu���������ƽ�������ת������ʵ�ֶ�����Ŀ��ƣ�ʵ����ʹ�õ���simple_switch.py����ʵ����һ���򵥵���ѧϰ��������������Ϻ�������h1�����м�socketͨ�ŵ�client����������2������sever�����ں����ʵ�ֿ��ƽڵ�����ͨ�ڵ������䡣
## ��������
��ݮ����̨��adhoc�����ɹ���[�ο�����](https://blog.csdn.net/lby0910/article/details/53420459)   
�����ƽڵ����ݮ�ɰ�װryu��������  
������ݮ�ɰ�װOVS��[�ο�����](https://www.cnblogs.com/goldsunshine/p/10331606.html)
## ����
### ���ƽڵ���ݮ��:  IP = 10.0.0.1  
������������
```
ryu-manager simple_switch.py
```
OVS����ز�����Ҫ�������Աģʽ��
```
sudo su
```  
����OVS
```
export PATH=$PATH:/usr/local/share/openvswitch/scripts
ovs-ctl start 
```

������������
```
ovs-vsctl add-br s1
```
����������Ӷ˿ڣ�  
��һ�лᱨ�����Լ��ɡ�
```
ovs-vsctl add-port s1 p1 
ovs-vsctl set Interface p1 ofport_request=1
ovs-vsctl set Interface p1 type=internal
```
����������
```
ip netns add h1
```
���������ӵ���������������IP��  
```
ip link set p1 netns h1   
ip netns exec h1 ip addr add 10.0.0.3/24 dev p1  
ip netns exec h1 ifconfig p1 promisc up
```
�����������ҽӵ���������һ���˿ڣ�
```
ovs-vsctl add-port s1 wlan0
```
wlan0�ҽӵ���������ԭIPʧЧ���뽻���������Ķ˿�s1��һ�������������������������ݰ�����wlan0��IP��ַת��s1�ϣ��൱�ڴ��������ݰ���������wlan0������s1��
```
ifconfig wlan0 0
ifconfig s1 10.0.0.1
ifconfig s1 up
```
���������ӿ�������
```
ovs-vsctl set-controller s1 tcp:10.0.0.1:6653
```
### ��ͨ�ڵ���ݮ��:  IP = 10.0.0.2

OVS����ز�����Ҫ�������Աģʽ��
```
sudo su
```  
����OVS
```
export PATH=$PATH:/usr/local/share/openvswitch/scripts
ovs-ctl start 
```
������������
```
ovs-vsctl add-br s2
```
����������Ӷ˿ڣ�  
��һ�лᱨ�����Լ��ɡ�
```
ovs-vsctl add-port s2 p2
ovs-vsctl set Interface p2 ofport_request=1
ovs-vsctl set Interface p2 type=internal
```
����������
```
ip netns add h2
```
���������ӵ���������������IP��  
```
ip link set p2 netns h2   
ip netns exec h2 ip addr add 10.0.0.4/24 dev p4  
ip netns exec h2 ifconfig p2 promisc up   
```
�����������ҽӵ���������һ���˿ڣ�
```
ovs-vsctl add-port s2 wlan0
```
��wlan0��IP��ַת��s2�ϣ�
```
ifconfig wlan0 0
ifconfig s2 10.0.0.2
ifconfig s2 up
```
���������ӿ�������
```
ovs-vsctl set-controller s2 tcp:10.0.0.1:6653
```

## ����

h1 ping h2��
```
ip netns exec h1 ping 10.0.0.6
```
h1��h2����socketͨ�ţ��ֱ��ڿ��ƽڵ����ͨ�ڵ����У�
```
ip netns exec h1 python3 SDN_on_Raspberry_pi/client.py
ip netns exec h2 python3 SDN_on_Raspberry_pi/sever.py
```

## �ο�����  
���Ĳο����°����������ڣ�  
[����ݮ���ϴad-hoc����̳�](https://blog.csdn.net/lby0910/article/details/53420459)   
[OVS�����̳̣�ʹ��Open vSwitch������������](https://www.sdnlab.com/sdn-guide/14747.html)  
[Open vSwitchϵ��֮�� ��װָ���汾ovs](https://www.cnblogs.com/goldsunshine/p/10331606.html)  
[ovs֮����ʵ��](https://www.cnblogs.com/mrwuzs/p/10242737.html)  
[SDNϵ��ѧϰ�γ�-OpenFlow-Ryu-Mininet](https://www.bilibili.com/video/BV1ft4y1a7ip?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click)  
[TCP/IP����ͨ��֮Socket�������](https://www.bilibili.com/video/BV1eg411G7pW?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click)  
��лһͬ�ܶ��ļ������ǡ�