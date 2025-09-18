#include "render.h"
#include <fxcg/display.h>


void ClearScreen() {
    Bdisp_Fill_VRAM(COLOR_WHITE, 3);
}

void FillScreen(int color, int mode) {
    Bdisp_Fill_VRAM(color, mode);
}
void UpdateDisplay() {
    Bdisp_PutDisp_DD();
}
