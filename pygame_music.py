import pygame
import sys

# 白
WHITE = (255, 255, 255)
# 黒
BLACK = (0, 0, 0)
# シアン
CYAN = (0, 255, 255)

def main():
    # pygameモジュールの初期化
    pygame.init()
    # ウィンドウに表示されるタイトルを設定
    pygame.display.set_caption("初めてのPygame キー入力")
    # スクリーンを初期化
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    try:
        # BGMを読み込む
        pygame.mixer_music.load("pygame_bgm.ogg")
        # SEを読み込む
        se = pygame.mixer.Sound("pygame_se.ogg")
    except:
        print("oggファイルが見当たらないか、オーディオ機器が接続されていません")

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
        # 「P」キー
        if key[pygame.K_p] == 1:
            # 再生中かどうか
            if pygame.mixer_music.get_busy() == False:
                # BGM再生（-1：ループ再生、１~ｎ：１＋（１~ｎ）回再生、）
                pygame.mixer_music.play(1)
        # 「S」キー
        if key[pygame.K_s] == 1:
            # 再生中かどうか
            if pygame.mixer_music.get_busy() == True:
                # BGM停止
                pygame.mixer_music.stop()
        # 「SPACE」キー
        if key[pygame.K_SPACE] == 1:
            # SE再生
            se.play()

        pos = pygame.mixer_music.get_pos()
        txt1 = font.render("BGM pos"+str(pos), True, WHITE)
        txt2 = font.render("[P]lay bgm : [S]top bgm : [SPACE] se", True, CYAN)
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
