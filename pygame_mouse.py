import pygame
import sys

# 黒
BLACK = (0, 0, 0)
# 青
LBLUE = (0, 192, 255)
# ピンク
PINK = (255, 0, 224)


def main():
    # pygameモジュールの初期化
    pygame.init()
    # ウィンドウに表示されるタイトルを設定
    pygame.display.set_caption("初めてのPygame マウス入力")
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

        # マウスポインタの座標を変数に代入
        mouseX, mouseY = pygame.mouse.get_pos()
        txt1 = font.render("{},{}".format(mouseX, mouseY), True, LBLUE)

        mBtn1, mBtn2, mBtn3 = pygame.mouse.get_pressed()
        txt2 = font.render("{}:{}:{}".format(mBtn1, mBtn2, mBtn3), True, PINK)

        # 指定色でスクリーン全体をクリア
        screen.fill(BLACK)
        # 文字列を描いたＳｕｒｆａｃｅをスクリーンに貼り付ける
        screen.blit(txt1, [100, 100])
        screen.blit(txt2, [100, 200])
        # 画面更新
        pygame.display.update()
        # フレームレートを設定する
        clock.tick(10)


if __name__ == "__main__":
    main()
