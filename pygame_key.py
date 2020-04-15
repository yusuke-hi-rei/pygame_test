import pygame
import sys

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


def main():
    # pygameモジュールの初期化
    pygame.init()
    # ウィンドウに表示されるタイトルを設定
    pygame.display.set_caption("初めてのPygame キー入力")
    # スクリーンを初期化
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 60)
    # 時間管理変数
    tmr = 0

    while True:
        # pygameのイベントを繰り返しで処理する
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # ウィンドウの✖ボタンをクリック
                # pygameのモジュールの初期化を解除
                pygame.quit()
                # プログラムを終了
                sys.exit()

        # リストkeyに全てのキー状態を代入
        key = pygame.key.get_pressed()
        txt1 = font.render("UP"+str(key[pygame.K_UP])+ " DOWN"+str(key[pygame.K_DOWN]), True, WHITE, GREEN)
        txt2 = font.render("LEFT"+str(key[pygame.K_LEFT])+ " RIGHT"+str(key[pygame.K_RIGHT]), True, WHITE, BLUE)
        txt3 = font.render("SPACE"+str(key[pygame.K_SPACE])+ " ENTER"+str(key[pygame.K_RETURN]), True, WHITE, RED)

        # 指定色でスクリーン全体をクリア
        screen.fill(BLACK)
        # 文字列を描いたＳｕｒｆａｃｅをスクリーンに貼り付ける
        screen.blit(txt1, [100, 100])
        screen.blit(txt2, [100, 200])
        screen.blit(txt3, [100, 300])
        # 画面更新
        pygame.display.update()
        # フレームレートを設定する
        clock.tick(10)


if __name__ == "__main__":
    main()
