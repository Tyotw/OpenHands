#!/usr/bin/env python3
import http.server
import os
import socketserver
import sys

# 设置端口
PORT = 12001

# 切换到游戏目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加CORS头部以支持跨域访问
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        # 添加安全头部
        self.send_header('X-Frame-Options', 'ALLOWALL')
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()

    def log_message(self, format, *args):
        # 自定义日志格式
        print(f'[{self.log_date_time_string()}] {format % args}')


if __name__ == '__main__':
    try:
        with socketserver.TCPServer(('0.0.0.0', PORT), MyHTTPRequestHandler) as httpd:
            print('🐍 精美贪吃蛇游戏服务器启动成功!')
            print(f'🌐 本地访问: http://localhost:{PORT}')
            print(
                '🌐 外部访问: https://work-2-kwqfirawkwuyaaaj.prod-runtime.all-hands.dev'
            )
            print(f'📁 服务目录: {os.getcwd()}')
            print('🎮 按 Ctrl+C 停止服务器')
            print('-' * 50)

            httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n🛑 服务器已停止')
        sys.exit(0)
    except Exception as e:
        print(f'❌ 服务器启动失败: {e}')
        sys.exit(1)
