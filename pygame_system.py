import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    # pygameモジュールの初期化
    pygame.init()
    # ウィンドウに表示されるタイトルを設定
    pygame.display.set_caption("初めてのPygame")
    # スクリーンを初期化
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)
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
        # Ｓｕｒｆａｃｅを作成。Ｓｕｒｆａｃｅに文字列を描く
        txt = font.render(str(tmr), True, WHITE)
        # 指定色でスクリーン全体をクリア
        screen.fill(BLACK)
        # 文字列を描いたＳｕｒｆａｃｅをスクリーンに貼り付ける
        screen.blit(txt, [300, 200])
        # 画面更新
        pygame.display.update()
        # フレームレートを設定する
        clock.tick(10)


if __name__ == "__main__":
    main()