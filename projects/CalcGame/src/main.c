#include <fxcg/display.h>
#include <fxcg/keyboard.h>
#include <stdio.h>

int main() {
    EnableStatusArea(3);
    Bdisp_EnableColor(1);
    int key;
    Bdisp_Fill_VRAM(COLOR_CYAN, 3);
    DrawFrame(COLOR_CYAN);
    Bdisp_PutDisp_DD();
    while (1) {
        
        GetKey(&key);
        if (key == KEY_CTRL_EXE) {
            break;
        }
        if(key) {
            Bdisp_Fill_VRAM(COLOR_CYAN, 3);
            char resualt[25];
            char *pre = "key id: ";
            sprintf(resualt, "%s%d", pre, key);
            int l;
            for(l = 0; resualt[l] != '\0'; l++);
            int xa = 0;
            int ya = 0;
            PrintMini(&xa, &ya, resualt, 0x02, 0xFFFFFFFF, 0, 0, COLOR_BLACK, COLOR_BLUE, 1, 0);
            Bdisp_PutDisp_DD();
        }
    }
 
    return 0;
}

void render() {
    Bdisp_Fill_VRAM(COLOR_CYAN, 3);
}