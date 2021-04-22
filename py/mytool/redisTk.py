#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis as rd


def connRedis(config,testShow):
    myRedis = rd.Redis(host=config['redis1_ip'], port=(config['redis1_port']), db=0, password=int(config['redis1_pw']),
                       decode_responses=True)
    try:
        myRedis.ping()
    except:
        testShow.set('redis 连接错误')
        return
    return myRedis

def hitDelRedis(redis,delCfg,testShow):
    try:
        redis.ping()
    except:
        testShow.set('redis 连接错误')
        return
    with open(delCfg, "r") as del_redis_key:
        for line in del_redis_key.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            redis.delete(line);
            testShow.set('删除 redis')






















