import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#背景の作成
    kk_image = pg.image.load("fig/3.png") #練習３：こうかとんsurfaceの作成
    kk_image = pg.transform.flip(kk_image, True, False) #練習３：こうかとんの左右反転
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習8：背景画像の左右反転
    kk_rct = kk_image.get_rect() #10-1：こうかとんのrctの取得
    kk_rct.center = (300, 200) #10-2：こうかとんの位置を指定

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #10-3：押下キーの取得]
        if key_lst[pg.K_UP]:
            kk_rct.move_ip(0, -1) #10-4：こうかとんの上移動

        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip(0, +1) #10-4：こうかとんの下移動 

        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip(-1, 0) #10-4：こうかとんの左移動

        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip(+10, 0) #10-4：こうかとんの右移動        
        
        x = tmr % 3200 #練習6：背景画像のループ
        screen.blit(bg_img, [-x, 0])#練習5：背景画像を右から左へ
        screen.blit(bg_img2, [-x + 1600, 0])#練習7：背景画像をループさせる
        screen.blit(bg_img2, [-x+3200, 0])#練習8：反転した背景画像の表示
        screen.blit(kk_image, kk_rct) #練習３：こうかとんの表示

        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()