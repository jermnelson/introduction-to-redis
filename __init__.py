"""
Name:        Redis Training Web App
Purpose:     Web front-end for Redis Training

Author:      Jeremy Nelson

Created:     2014/22/08
Copyright:   (c) Jeremy Nelson 2014
Licence:
"""
__version_info__ = ('0', '1', '1')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = ''
__copyright__ = '(c) 2014 by Jeremy Nelson'

import os
import re
import sys
from flask import Flask, render_template, abort
from collections import OrderedDict

TOPICS = OrderedDict([
    ('introducing-redis', {
        'location': 'introducing-redis',
        'title': 'Introducing Redis'}),
    ('basic-setup-and-admin', {
        'location': 'basic-setup-and-admin',
        'title': 'Basic Setup and Admin'}),
    ('redis-data-types', {
        'location': 'redis-data-types',
        'title': 'Redis data types'}),
    ('operating-a-redis-system', {
        'location': 'operating-a-redis-system',
        'title': 'Operating a Redis System'}),
    ('replication-and-pubsub', {
        'location': 'replication-and-pubsub',
        'title': 'Replication and Pub/Sub'}),
    ('pipelining-and-mass-insertions', {
        'location': 'pipelining-and-mass-insertions',
        'title': 'Pipelining and Mass Insertions of Data'}),
    ('memory-expiration-and-key-eviction', {
        'location': 'memory-expiration-and-key-eviction',
        'title': 'Memory, expiration and key eviction'}),
    ('transactions-and-locks', {
        'location': 'transactions-and-locks',
        'title': 'Transactions and Locks'}),
    ('programming-redis', {
        'location': 'programming-redis',
        'title': 'Programming Redis'}),
    ('lua-scripting', {
        'location': 'lua-scripting',
        'title': 'Lua Scripting'}),
    ('clustering-and-ha', {
        'location': 'clustering-and-ha',
        'title': 'Clustering and High Availability'}),
    ('security', {
        'location': 'security',
        'title': 'Security and Coming Features'})])

TOPIC_ORDER = list(TOPICS.keys())

app = Flask(__name__)


name_re = re.compile(r"(.*).(tar.gz|zip)") 
@app.template_filter('latest_redis')
def latest_redis(s):
    """Template filter returns active download url and name of 
    Redis version being used in the course with Windows download
    as well."""
    info = {}
    info['url'] = "https://github.com/antirez/redis/archive/3.0.0-rc4.tar.gz"
    info['filename'] = "3.0.0-rc4.tar.gz"
    info['name'] = "redis-3.0.2"  
    info['win'] = {"url": "https://github.com/MSOpenTech/redis/releases/download/win-2.8.19/redis-2.8.19.zip",
                   "filename": "redis-2.8.19.zip"}
    info['win']['name'] = name_re.search(info['win']['filename']).groups()[0]
    return info

@app.route("/badge")
def badge():
    return render_template(
        'badge.html',
        section='badge',
        topics=TOPICS)

@app.route("/contact")
def contact():
    return render_template(
        'contact.html',
        section='contact',
        topics=TOPICS)

@app.route("/redis-virtual-machine")
@app.route("/redis-vm")
def redis_course_vm():
    return render_template(
        'redis-training-vm.html',
        section='topic',
        topics=TOPICS)

@app.route("/<topic>")
def topic_view(topic):
    if not topic in TOPICS:
        abort(404)
    position = TOPIC_ORDER.index(topic)
    next_topic, previous_topic = None, None
    if position+1 < len(TOPIC_ORDER):
        next_topic = {
            'key': TOPIC_ORDER[position+1],
            'title': TOPICS[TOPIC_ORDER[position+1]]['title']}
    if position-1 >= 0:
        previous_topic = {
            'key': TOPIC_ORDER[position-1],
            'title': TOPICS[TOPIC_ORDER[position-1]]['title']
            }
    return render_template(
        "{}.html".format(topic),
        section='topic',
        next=next_topic,
        previous=previous_topic,
        topics=TOPICS)

@app.route("/")
def home():
    return render_template("index.html",
        section='home',
        topics=TOPICS)

def main():
    host = '0.0.0.0'
    port = 8023
    app.run(
        debug=True,
        host=host,
        port=port
    )

if __name__ == '__main__':
    main()
