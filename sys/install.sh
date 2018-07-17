#!/bin/bash

cp -v -r ../kapbot /usr/share/kaplanbot
cp -v kaplanbot.sh /usr/bin/kaplanbot.sh
cp -v kaplanbot.service /etc/systemd/system/kaplanbot.service

chmod -v +x /usr/bin/kaplanbot.sh
chmod -v +x /etc/systemd/system/kaplanbot.service



