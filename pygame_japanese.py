"""
 Pygameは日本語の表示が苦手。日本語を表示するには、print(pygame.font.get_fonts())で
 各パソコンで使用できる日本語フォントを調べ、それを指定する方法があるが、
 Pygameで使える日本語フォントはPCごとに違ううえ、種類が限られている。
 そこでIPAフォントを用いて日本語を表示する方法がある。
"""

import pygame
import sys

# 白
WHITE = (255, 255, 255)
# 黒
BLACK = (0, 0, 0)


def main():
    # pygameモジュールの初期化
    pygame.init()
    # ウィンドウに表示されるタイトルを設定
    pygame.display.set_caption("初めてのPygameで日本語を表示する")
    # スクリーンを初期化
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font("ipam00303/ipam.ttf", 80)
    # 時間管理変数
    tmr = 0

    while True:
        tmr = tmr + 1
        # pygameのイベントを繰り返しで処理する
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # ウィンドウの✖ボタンをクリック
                # pygameのモジュールの初期化を解除
                pygame.quit()
                # プログラムを終了
                sys.exit()
        txt = font.render("日本語表示 "+str(tmr), True, WHITE)

        # 指定色でスクリーン全体をクリア
        screen.fill(BLACK)
        # 文字列を描いたＳｕｒｆａｃｅをスクリーンに貼り付ける
        screen.blit(txt, [100, 100])
        # 画面更新
        pygame.display.update()
        # フレームレートを設定する
        clock.tick(10)


if __name__ == "__main__":
    main()
