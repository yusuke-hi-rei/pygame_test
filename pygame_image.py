import pygame
import sys


def main():
    # pygameモジュールの初期化
    pygame.init()
    # ウィンドウに表示されるタイトルを設定
    pygame.display.set_caption("初めてのPygame画像表示")
    # スクリーンを初期化
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()

    # キャラクタ画像の読み込み
    img_bg = pygame.image.load("pg_bg.png")
    img_chara = [
        pygame.image.load("pg_chara0.png"),
        pygame.image.load("pg_chara1.png"),
    ]

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
            if event.type == pygame.KEYDOWN:
                # フルスクリーンモード
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)
                # 通常表示
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((640, 360))
        # 背景スクロール用の値をtmrから計算する
        x = tmr % 160
        # 繰り返しで５回分の背景画像を描画する
        for i in range(5):
            screen.blit(img_bg, [i*160-x, 0])
        # キャラクタをアニメーションさせて描画
        screen.blit(img_chara[tmr%2], [224, 160])

        # 画面更新
        pygame.display.update()
        # フレームレートを設定する
        clock.tick(5)


if __name__ == "__main__":
    main()