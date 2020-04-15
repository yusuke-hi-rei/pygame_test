import pygame
import sys
import math

# 白
WHITE = (255, 255, 255)
# 黒
BLACK = (0, 0, 0)
# 赤
RED = (255, 0, 0)
# 緑
GREEN = (0, 255, 0)
# 青
BLUE = (0, 0, 255)
# 金
GOLD = (255, 216, 0)
# 銀
SILVER = (192, 192, 192)
# 銅
COPPER = (192, 112, 48)


def main():
    # pygameモジュールの初期化
    pygame.init()
    # ウィンドウに表示されるタイトルを設定
    pygame.display.set_caption("初めてのPygame 図形")
    # スクリーンを初期化
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
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
        # 指定色でスクリーン全体をクリア
        screen.fill(BLACK)
        # 線の描画
        pygame.draw.line(screen, RED, [0, 0], [100,200], 10)
        pygame.draw.lines(screen, BLUE, False, [[50,300], [150,400], [50,500]])
        # 矩形の描画
        pygame.draw.rect(screen, RED, [200,50,120,80])
        pygame.draw.rect(screen, GREEN, [200,200,60,180], 5)
        # 多角形の描画
        pygame.draw.polygon(screen, BLUE, [[250,400], [200,500], [300,500]], 10)
        # 円の描画
        pygame.draw.circle(screen, GOLD, [400,100], 60)
        # 楕円の描画
        pygame.draw.ellipse(screen, SILVER, [400-80, 300-40, 160,80])
        pygame.draw.ellipse(screen, COPPER, [400-40, 500-80, 80,160], 20)

        # 円弧の角度計算（弧度計算）
        ang = math.pi * tmr / 36
        pygame.draw.arc(screen, BLUE, [600-100, 300-200, 200, 400], 0, math.pi*2)
        pygame.draw.arc(screen, WHITE, [600-100, 300-200, 200, 400], ang, ang+math.pi/2, 8)

        # 画面更新
        pygame.display.update()
        # フレームレートを設定する
        clock.tick(10)


if __name__ == "__main__":
    main()