#ifndef _RENDER_H
#define _RENDER_H

#ifdef __cplusplus
extern "C" {
#endif



void ClearScreen();
void FillScreen( int color, int mode );
void UpdateDisplay();
void DisplayText( int x_start, int y_start, const char *text, int mode_flags, unsigned int xlimit, int unknown1, int unknown2, int color, int back_color, int writeflag, int unknown3);//use PrintMini
void Rect();//use DirectDrawRectangle

#ifdef __cplusplus
}
#endif

#endif