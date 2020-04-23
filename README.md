# 需要用到的微服务

app-test.py 需要演示者再次单独配置



### app.py 一个单独的服务

直接用就行了

### app-test.py 配合容器调度的服务

需要修改nginx的ip地址即源码中redis的地址

源码里面使用的参数在本机上测试时，redis的cpu压力最高为10.6%，稳定在5%或者9%。

部分参数说明

test.html中每7秒发送一次插入请求（7秒为本人在自己电脑上测的比较中和的值）接收一个插入使用时间的值并显示，本机测试为13或14秒。每7秒发送一个请求每14或14秒才能收到请求，所以一定会产生阻塞，产生阻塞后python做了一些调整使程序再次运行。

app-test.py 中循环1000次，每次生成一个redis对象，该redis对象随机向一个redis数据库插入20条数据，这20条数据不是随机插入，只会插入到一个redis数据库中。最后统计每次函数运行的时间并返回给前端。

### nginx容器配置

redis不需要配置，端口映射了就可以直接用

开启nginx容器时端口映射8080:80 和 6379:6379

容器跑起来后先

`apt-get update`

`apt-get install vim`

保证能够正常编辑文件

下一步到容器内的配置文件

`vim /etc/nginx/nginx.conf`

在末尾添加

```
stream {
    upstream redis {
        server 192.168.2.108:63791;
        server 192.168.2.108:63792;
    }
    server {
        listen 6379;
        proxy_pass redis;
    }
}
```

server可以放好多redis，端口建议按照顺序依次排布。

配置好后重启容器就生效了。