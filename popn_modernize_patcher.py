#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PS2 pop'n music 7〜14 / BEST HITS 用 pnach ジェネレータ (標準ライブラリのみ / Python 3.8+)

PCSX2 の patches フォルダにある既存 pnach (ハイスピード拡張・判定調整・キービーム等) の
実コードをタイトルごとに内蔵し、チェックした機能だけを pnach として出力します。
数値で指定できる項目（COOL 判定幅・キービーム長・レーン明度・判定タイミング）は GUI で入力。

  python popn_modernize_patcher.py             GUI 起動
  python popn_modernize_patcher.py --selftest  内蔵データの整合テスト
"""
import json
import os
import re
import sys

VERSION = "1.0"

# exe 化 (PyInstaller) 時は exe のあるフォルダ、通常はスクリプトのフォルダ
if getattr(sys, "frozen", False):
    if sys.platform == "darwin":  # .app 内には書き込まない
        APP_DIR = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "popn_modernize_patcher")
        os.makedirs(APP_DIR, exist_ok=True)
    else:
        APP_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    APP_DIR = os.path.dirname(os.path.abspath(__file__))
from collections import OrderedDict

TITLES = OrderedDict([
    ("pop'n music 7",         "SLPM-65208_459970FC"),
    ("pop'n music 8",         "SLPM-65316_18B64A1A"),
    ("pop'n music 9",         "SLPM-65508_DFBAFDE3"),
    ("pop'n music 10",        "SLPM-65770_088871A6"),
    ("pop'n music 11",        "SLPM-66065_47F66D02"),
    ("pop'n music 12",        "SLPM-66314_35E0596E"),
    ("pop'n music 13",        "SLPM-66533_4BD5C7E6"),
    ("pop'n music 14 FEVER!", "SLPM-66742_632DB211"),
    ("pop'n music BEST HITS", "SLPM-62288_098E1539"),
])
SERIAL_TO_NAME = {v: k for k, v in TITLES.items()}

# 既存 pnach から抽出した内蔵データ: {serial: {gametitle, sections:[{id,name,lines}]}}
DATA = json.loads(r'''{
"SLPM-65208_459970FC": {
"gametitle": "gametitle=pop'n music 7 (CRC 459970FC)",
"sections": [
{
"name": "HiSpeed x2-x8 with .5 steps (to x7.5)",
"id": "hispeed",
"lines": [
"comment=OFF→2→2.5→…→7.5→8→OFF。表示はx5→x2, x6→x3, x7/x8→x4（.5は元の段階の表示）",
"patch=1,EE,0013B480,word,0000482D",
"patch=1,EE,0013B484,word,1080000B",
"patch=1,EE,0013B488,word,24830003",
"patch=1,EE,0013B48C,word,00031842",
"patch=1,EE,0013B490,word,24630002",
"patch=1,EE,0013B494,word,24090001",
"patch=1,EE,0013B498,word,00694804",
"patch=1,EE,0013B49C,word,30830001",
"patch=1,EE,0013B4A0,word,14600004",
"patch=1,EE,0013B4A4,word,00000000",
"patch=1,EE,0013B4A8,word,35290800",
"patch=1,EE,0013B4AC,word,00000000",
"patch=1,EE,0013B4B0,word,00000000",
"patch=1,EE,0013B43C,word,000322C2",
"patch=1,EE,0013B440,word,30840001",
"patch=1,EE,0013B444,word,306307F0",
"patch=1,EE,0013B448,word,10600005",
"patch=1,EE,0013B44C,word,0000102D",
"patch=1,EE,0013B450,word,2482FFF7",
"patch=1,EE,0013B454,word,00031842",
"patch=1,EE,0013B458,word,1460FFFE",
"patch=1,EE,0013B45C,word,24420002",
"patch=1,EE,0013B460,word,03E00008",
"patch=1,EE,0013B464,word,00000000",
"patch=1,EE,0013B468,word,3C01EAA5",
"patch=1,EE,0013B46C,word,34210A50",
"patch=1,EE,0013B470,word,00031840",
"patch=1,EE,0013B474,word,00611806",
"patch=1,EE,0013B478,word,30630003",
"patch=1,EE,0013B47C,word,08056ECC",
"patch=1,EE,001395F4,word,2862000D",
"patch=1,EE,00139670,word,8F8382A4",
"patch=1,EE,00139674,word,0C04ED1A",
"patch=1,EE,00139678,word,00000000",
"patch=1,EE,0013967C,word,3C02001A",
"patch=1,EE,00139680,word,00431021",
"patch=1,EE,00139684,word,8C4559A0",
"patch=1,EE,001397B8,word,8F8382A4",
"patch=1,EE,001397BC,word,0C04ED1A",
"patch=1,EE,001397C0,word,2463FFFF",
"patch=1,EE,001397C4,word,3C02001A",
"patch=1,EE,001397C8,word,00431021",
"patch=1,EE,001397CC,word,8C4559A0",
"patch=1,EE,0013A124,word,0C04ED1A",
"patch=1,EE,0013A128,word,2483FFFF",
"patch=1,EE,0013A12C,word,14600014",
"patch=1,EE,0013A180,word,2463FFF8",
"patch=1,EE,0013A184,word,04610014",
"patch=1,EE,0013A1D8,word,1C600013",
"patch=1,EE,0014C474,word,30620640",
"patch=1,EE,0015BAE8,word,308307F0",
"patch=1,EE,0015BAEC,word,1060000D",
"patch=1,EE,0015BAF0,word,24023FF0",
"patch=1,EE,0015BAF4,word,00042AC2",
"patch=1,EE,0015BAF8,word,30A50001",
"patch=1,EE,0015BAFC,word,24A5FFFA",
"patch=1,EE,0015BB00,word,00031842",
"patch=1,EE,0015BB04,word,1460FFFE",
"patch=1,EE,0015BB08,word,24A50002",
"patch=1,EE,0015BB0C,word,28A30008",
"patch=1,EE,0015BB10,word,10600003",
"patch=1,EE,0015BB14,word,00051040",
"patch=1,EE,0015BB18,word,00051080",
"patch=1,EE,0015BB1C,word,2442FFF0",
"patch=1,EE,0015BB20,word,24424000",
"patch=1,EE,0015BB24,word,00021C3C",
"patch=1,EE,0015BB28,word,10000004",
"patch=1,EE,0015BB2C,word,FF838470",
"patch=1,EE,0015BB30,word,03E00008",
"patch=1,EE,0015BB34,word,00031880",
"patch=1,EE,0015BB38,word,00000000",
"patch=1,EE,0014C458,word,30620090",
"patch=1,EE,0014C460,word,30620120"
]
},
{
"name": "Judge Timing Adjust",
"id": "jtime",
"lines": [
"author=Claude",
"description=判定タイミング調整。最後の行の下4桁(XXXX)が調整値で、1単位=4ms(16ビット符号付き)。0000=調整なし／FFFF=-4ms／FFFE=-8ms／FFFD=-12ms／FFFC=-16ms／FFFA=-24ms／FFF8=-32ms／0001=+4ms／0002=+8ms／0004=+16ms／0008=+32ms。マイナス=判定ラインが遅くなる(遅めに押してもジャスト)、プラス=判定ラインが早くなる。0x161534の daddu a1,s2,zero を addiu a1,s2,調整値 に置換(判定処理に渡す時刻だけをずらすので譜面表示と音はそのまま)。上4桁(2645)は変更しないこと。",
"patch=1,EE,00161534,word,2645FFF8"
]
},
{
"name": "COOL Judge in All Modes",
"id": "coolall",
"lines": [
"author=Claude",
"description=全モードでCOOL判定を有効化(GREAT範囲の中心±4でCOOL)し、スコア計算をCOOLありモード(モード2/6)の式にする(ただしGOODは0点ではなく100000)。COOLのゲージ増加量はGREATと同じ(COOLありモードは従来どおり0)。オートプレイ/デモもCOOLになる。画面下のカウンター欄を全モードでCOOL付きにする(フレームは各モードのまま)。",
"// 0x160F38: COOL判定のモード条件を常に成立",
"// 0x16008C: COOL判定の結果を全モードで処理(元はCOOLなしモードでは無視)",
"// 0x1600D0: COOL時のゲージ増減にGREATの値を使う",
"// 0x1613D4: オートプレイのCOOL条件を常に成立",
"// 0x161AF4: スコア満点を全モードでCOOLありモードの式に(ノーツ数x10)",
"// 0x160A2C-0x160A78: スコア加算をCOOLありモードの式に(COOL=1000000/GREAT=500000)し、GOODを追加(100000、元のCOOLなしモードの加算処理を流用)",
"// 0x14F870/0x14F8C0/0x14F8C4/0x14F8E8/0x14F8F8: 画面下のカウンター欄の重ね画像を全モードでCOOL付き(0x80032)に",
"// 0x14EEA8: 画面下の表示部品を常にCOOLありモードの形で作成",
"// 0x1A6780/0x1A6784/0x1A6790: リザルト画面のモード別初期化テーブルを差し替え、通常版(0x146D50)の代わりにCOOL付き版(0x145A30)を使う(バトルは対象外)",
"// 0x1A67A0/0x1A67A4/0x1A67B0: リザルト画面のモード別読み込みテーブルも差し替え、通常版の素材(0x1A系、0x1474F0)の代わりにCOOL付き版の素材(0x1B系、0x145FA0)を読み込む(初期化だけ差し替えると素材が合わず表示が崩れるため)",
"patch=1,EE,0014EEA8,word,10000006",
"patch=1,EE,0014F870,word,34700032",
"patch=1,EE,0014F8C0,word,34B00032",
"patch=1,EE,0014F8C4,word,34A30032",
"patch=1,EE,0014F8E8,word,34700032",
"patch=1,EE,0014F8F8,word,34700032",
"patch=1,EE,0016008C,word,00000000",
"patch=1,EE,001600D0,word,24040000",
"patch=1,EE,00160A2C,word,3C0200C2",
"patch=1,EE,00160A30,word,001118C0",
"patch=1,EE,00160A34,word,24425680",
"patch=1,EE,00160A38,word,00432021",
"patch=1,EE,00160A3C,word,DC830000",
"patch=1,EE,00160A40,word,3A410005",
"patch=1,EE,00160A44,word,14200006",
"patch=1,EE,00160A48,word,00000000",
"patch=1,EE,00160A60,word,12400006",
"patch=1,EE,00160A64,word,00000000",
"patch=1,EE,00160A68,word,3A410001",
"patch=1,EE,00160A6C,word,1420001C",
"patch=1,EE,00160A70,word,00000000",
"patch=1,EE,00160A74,word,10000016",
"patch=1,EE,00160A78,word,00000000",
"patch=1,EE,00160F38,word,00000000",
"patch=1,EE,001613D4,word,00000000",
"patch=1,EE,00161AF4,word,00000000",
"patch=1,EE,001A6780,word,00145268",
"patch=1,EE,001A6784,word,00145268",
"patch=1,EE,001A6790,word,00145268",
"patch=1,EE,001A67A0,word,00145374",
"patch=1,EE,001A67A4,word,00145374",
"patch=1,EE,001A67B0,word,00145374"
]
},
{
"name": "Score Formula (current pop'n)",
"id": "score",
"lines": [
"author=Claude",
"description=COOLありモードのスコア式を現行ポップンの式に変更: スコア=100000×(COOL×1.0+GREAT×0.7+GOOD×0.4)÷ポップ君総数(小数点以下切り捨て)。[COOL Judge in All Modes]と一緒に有効にすること(popn7はCOOLありモードの式にGOODの加算がないため単独では不完全)。",
"// 0x160A7C-0x160A80: GREATの加算値 500000 → 700000",
"// 0x160AD0-0x160AD4: GOODの加算値 100000 → 400000",
"patch=1,EE,00160A7C,word,3C02000A",
"patch=1,EE,00160A80,word,3442AE60",
"patch=1,EE,00160AD0,word,3C020006",
"patch=1,EE,00160AD4,word,34421A80"
]
},
{
"name": "No FEVER at Gauge MAX",
"id": "nofever",
"lines": [
"author=Claude",
"description=ゲージMAX時(および一部モードのコンボ99以上)にGREATがFEVER表示になるのを無効化し、常に通常のGREATとして表示する(スコアは元からGREATと同じ扱いなので変化なし)。",
"// 0x160174: FEVER判定の分岐を常に通常GREAT側へ",
"patch=1,EE,00160174,word,1000000A"
]
},
{
"name": "Key Beam Length",
"id": "keybeam",
"lines": [
"author=Claude",
"description=キービームの長さを変更する。下端(判定ライン側)は固定のまま上に向かって縮み、グラデーションも縮小される。「長さ」と書いた2行の値(末尾8桁)を下の表の同じ値に書き換えること。初期値は50%。",
"// 長さの値(2行とも同じ値にする。元の長さ=100%、ビームの高さは元257px)",
"//     0% = 00000000 (  0px)",
"//    10% = 0000000A ( 25px)",
"//    20% = 00000014 ( 51px)",
"//    30% = 0000001E ( 77px)",
"//    40% = 00000028 (102px)",
"//    50% = 00000032 (128px)",
"//    60% = 0000003C (154px)",
"//    70% = 00000046 (179px)",
"//    80% = 00000050 (205px)",
"//    90% = 0000005A (231px)",
"//   100% = 00000064 (257px)",
"// 仕組み: ビームはスプライトセット0のフレーム208-211(テクスチャ30x257)。キーフレーム0x9D8114-0x9D830C(間隔0x48)の",
"//   基準点Yとオフセットトラックの Y を257(スプライト下端)にし、Yスケールのトラックを空きRAMに置いた新しいトラックに差し替える。",
"//   0x000FFF00 = 幅100%のビーム用(横100%、縦=値)、0x000FFF10 = 幅80%のビーム用(横80%、縦=値)",
"// 次の5か所がプレイ画面のスプライトセットの値と一致するときだけ書き込む(Eコード。リザルト等の別画面では書き込まない)",
"//   0xBD0484=A4B0(セット0のデータ位置) / 0x9D8116=00D0(フレーム番号) / 0x9D8124=000F(基準点X) / 0x9D3ACA=000F / 0x9D3BA2=000C(トラックX)",
"patch=1,EE,E02CA4B0,extended,00BD0484",
"patch=1,EE,E02B00D0,extended,009D8116",
"patch=1,EE,E02A000F,extended,009D8124",
"patch=1,EE,E029000F,extended,009D3ACA",
"patch=1,EE,E028000C,extended,009D3BA2",
"// 長さ(幅100%のビーム)",
"patch=1,EE,200FFF04,extended,0000001E",
"// 長さ(幅80%のビーム)",
"patch=1,EE,200FFF14,extended,0000001E",
"// ここから下は変更しない",
"patch=1,EE,200FFF00,extended,00640000",
"patch=1,EE,200FFF08,extended,0000FFFF",
"patch=1,EE,200FFF0C,extended,00000000",
"patch=1,EE,200FFF10,extended,00500000",
"patch=1,EE,200FFF18,extended,0000FFFF",
"patch=1,EE,200FFF1C,extended,00000000",
"patch=1,EE,209D812C,extended,FF72FA80",
"patch=1,EE,209D81BC,extended,FF72FA80",
"patch=1,EE,209D824C,extended,FF72FA80",
"patch=1,EE,209D82DC,extended,FF72FA80",
"patch=1,EE,209D8174,extended,FF72FA90",
"patch=1,EE,209D8204,extended,FF72FA90",
"patch=1,EE,209D8294,extended,FF72FA90",
"patch=1,EE,209D8324,extended,FF72FA90",
"patch=1,EE,109D8126,extended,00000101",
"patch=1,EE,109D81B6,extended,00000101",
"patch=1,EE,109D8246,extended,00000101",
"patch=1,EE,109D82D6,extended,00000101",
"patch=1,EE,109D816E,extended,00000101",
"patch=1,EE,109D81FE,extended,00000101",
"patch=1,EE,109D828E,extended,00000101",
"patch=1,EE,109D831E,extended,00000101",
"patch=1,EE,109D3ACC,extended,00000101",
"patch=1,EE,109D3AD4,extended,00000101",
"patch=1,EE,109D3AE4,extended,00000101",
"patch=1,EE,109D3AEC,extended,00000101",
"patch=1,EE,109D3B0C,extended,00000101",
"patch=1,EE,109D3B14,extended,00000101",
"patch=1,EE,109D3B24,extended,00000101",
"patch=1,EE,109D3B2C,extended,00000101",
"patch=1,EE,109D3B4C,extended,00000101",
"patch=1,EE,109D3B54,extended,00000101",
"patch=1,EE,109D3B64,extended,00000101",
"patch=1,EE,109D3B6C,extended,00000101",
"patch=1,EE,109D3B8C,extended,00000101",
"patch=1,EE,109D3B94,extended,00000101",
"patch=1,EE,109D3BA4,extended,00000101",
"patch=1,EE,109D3BAC,extended,00000101"
]
},
{
"name": "Lane Brightness",
"id": "lane",
"lines": [
"comment=Darken the key lane background. Rewrite ONLY the value at 000FFA00 (hex, 00-64):",
"comment=  100%=00000064 (original)  90%=0000005A  80%=00000050  70%=00000046  60%=0000003C",
"comment=   50%=00000032  40%=00000028  30%=0000001E  20%=00000014  10%=0000000A  0%=00000000 (black)",
"comment=Default is 70%. Only the lane background is affected (not notes/beam).",
"patch=1,EE,000FFA00,word,00000032",
"patch=1,EE,00125CF0,word,0803FEC0",
"patch=1,EE,000FFB00,word,ADA000CC",
"patch=1,EE,000FFB04,word,8DA80090",
"patch=1,EE,000FFB08,word,8DA90094",
"patch=1,EE,000FFB0C,word,8DAA00C0",
"patch=1,EE,000FFB10,word,8DAB00C4",
"patch=1,EE,000FFB14,word,340C77F0",
"patch=1,EE,000FFB18,word,010C602B",
"patch=1,EE,000FFB1C,word,1580003B",
"patch=1,EE,000FFB20,word,00000000",
"patch=1,EE,000FFB24,word,340C6FF0",
"patch=1,EE,000FFB28,word,012C602B",
"patch=1,EE,000FFB2C,word,15800037",
"patch=1,EE,000FFB30,word,00000000",
"patch=1,EE,000FFB34,word,340C87A1",
"patch=1,EE,000FFB38,word,014C602B",
"patch=1,EE,000FFB3C,word,11800033",
"patch=1,EE,000FFB40,word,00000000",
"patch=1,EE,000FFB44,word,340C83D1",
"patch=1,EE,000FFB48,word,016C602B",
"patch=1,EE,000FFB4C,word,1180002F",
"patch=1,EE,000FFB50,word,00000000",
"patch=1,EE,000FFB54,word,01487823",
"patch=1,EE,000FFB58,word,2DEC07C0",
"patch=1,EE,000FFB5C,word,1580002B",
"patch=1,EE,000FFB60,word,00000000",
"patch=1,EE,000FFB64,word,2DEC07C1",
"patch=1,EE,000FFB68,word,11800028",
"patch=1,EE,000FFB6C,word,00000000",
"patch=1,EE,000FFB70,word,3C0C0010",
"patch=1,EE,000FFB74,word,8D8CFA00",
"patch=1,EE,000FFB78,word,240E0064",
"patch=1,EE,000FFB7C,word,8DA80080",
"patch=1,EE,000FFB80,word,010C0018",
"patch=1,EE,000FFB84,word,00004012",
"patch=1,EE,000FFB88,word,010E001A",
"patch=1,EE,000FFB8C,word,00004012",
"patch=1,EE,000FFB90,word,ADA80080",
"patch=1,EE,000FFB94,word,8DA80084",
"patch=1,EE,000FFB98,word,010C0018",
"patch=1,EE,000FFB9C,word,00004012",
"patch=1,EE,000FFBA0,word,010E001A",
"patch=1,EE,000FFBA4,word,00004012",
"patch=1,EE,000FFBA8,word,ADA80084",
"patch=1,EE,000FFBAC,word,8DA80088",
"patch=1,EE,000FFBB0,word,010C0018",
"patch=1,EE,000FFBB4,word,00004012",
"patch=1,EE,000FFBB8,word,010E001A",
"patch=1,EE,000FFBBC,word,00004012",
"patch=1,EE,000FFBC0,word,ADA80088",
"patch=1,EE,000FFBC4,word,8DA800B0",
"patch=1,EE,000FFBC8,word,010C0018",
"patch=1,EE,000FFBCC,word,00004012",
"patch=1,EE,000FFBD0,word,010E001A",
"patch=1,EE,000FFBD4,word,00004012",
"patch=1,EE,000FFBD8,word,ADA800B0",
"patch=1,EE,000FFBDC,word,8DA800B4",
"patch=1,EE,000FFBE0,word,010C0018",
"patch=1,EE,000FFBE4,word,00004012",
"patch=1,EE,000FFBE8,word,010E001A",
"patch=1,EE,000FFBEC,word,00004012",
"patch=1,EE,000FFBF0,word,ADA800B4",
"patch=1,EE,000FFBF4,word,8DA800B8",
"patch=1,EE,000FFBF8,word,010C0018",
"patch=1,EE,000FFBFC,word,00004012",
"patch=1,EE,000FFC00,word,010E001A",
"patch=1,EE,000FFC04,word,00004012",
"patch=1,EE,000FFC08,word,ADA800B8",
"patch=1,EE,000FFC0C,word,0804973D",
"patch=1,EE,000FFC10,word,00000000"
]
},
{
"name": "COOL Window 25ms",
"id": "coolwin",
"lines": [
"author=Claude",
"description=COOL判定の幅を±16ms(内部値±4)から現行ポップンの±25ms(内部値±6)に広げる。判定結果を決める処理の中で「時間差が-4以上かつ4以下ならCOOL」と比較している即値(-4と5)を(-6と7)に書き換えるだけで、GREAT以下の判定幅とスコア式は変えない。",
"// 内部の時間単位は1/240秒(約4.17ms)。COOL ±4=±16.7ms → ±6=±25.0ms。",
"// このタイトルのGREAT幅は内部値±8(約±33.3ms)なので、COOL ±6はGREATの内側に収まる。",
"// 幅を変えたい場合: 「-4」の行の末尾4桁を(-N)の16ビット値、「5」の行の末尾4桁を(N+1)に書き換える。",
"//   N=4(元)  FFFC / 0005    N=5  FFFB / 0006    N=6(25ms)  FFFA / 0007    N=7  FFF9 / 0008",
"// 「-4」の行は slti(時間差 < -N)、「5」の行は slti(時間差 < N+1)。「-4」の行が2つあるタイトルは、分岐の遅延スロットに入った同じ比較の複製(両方書き換える)。",
"patch=1,EE,00160F3C,word,2A42FFFA",
"patch=1,EE,00160F44,word,2A410007"
]
},
{
"name": "480p Test (experimental)",
"id": "p480",
"lines": [
"author=Claude",
"comment=実験用。起動時にゲームを最初から起動すること（ステートのロードでは反映されない）。sceGsResetGraph を 480i→480p(inter=0, omode=0x50, ffmd=1) に変更 し、毎フレームの DISPLAY 定数を 480p 用(DX=440 DY=35 MAGH=2倍 DW=1023 DH=447)にする。512幅のまま出力するため、PCSX2 側でアスペクト比を 4:3 にして使う。",
"patch=1,EE,00129790,word,24050000",
"patch=1,EE,00129794,word,24060050",
"patch=1,EE,0012979C,word,24070001",
"patch=1,EE,0012A098,word,3443F3FF",
"patch=1,EE,0012A09C,word,3C020082",
"patch=1,EE,0012A0A4,word,344331B8",
"patch=1,EE,0012A0A8,word,344231B8"
]
}
]
},
"SLPM-65316_18B64A1A": {
"gametitle": "gametitle=pop'n music 8 (CRC 18B64A1A)",
"sections": [
{
"name": "HiSpeed x2-x8 with .5 steps (to x7.5)",
"id": "hispeed",
"lines": [
"author=Claude",
"comment=OFF→2→2.5→…→7.5→8→OFF。表示はx5→x2, x6→x3, x7/x8→x4（.5は元の段階の表示）。2曲目以降のオプション画面初期表示もx5以上に対応",
"patch=1,EE,0015FCF0,word,0000502D",
"patch=1,EE,0015FCF4,word,0000582D",
"patch=1,EE,0015FCF8,word,0000602D",
"patch=1,EE,0015FCFC,word,3C033FF0",
"patch=1,EE,0015FD00,word,3C0700C4",
"patch=1,EE,0015FD04,word,0003203C",
"patch=1,EE,0015FD08,word,3C090187",
"patch=1,EE,0015FD0C,word,24E78CB0",
"patch=1,EE,0015FD10,word,2529AEC0",
"patch=1,EE,0015FD14,word,00000000",
"patch=1,EE,0015FD18,word,00000000",
"patch=1,EE,0015FD1C,word,00000000",
"patch=1,EE,0015FD20,word,012B1821",
"patch=1,EE,0015FD24,word,8C6D0010",
"patch=1,EE,0015FD28,word,00EC7021",
"patch=1,EE,0015FD2C,word,31A201FC",
"patch=1,EE,0015FD30,word,10400012",
"patch=1,EE,0015FD34,word,70401004",
"patch=1,EE,0015FD38,word,2403001E",
"patch=1,EE,0015FD3C,word,00621023",
"patch=1,EE,0015FD40,word,2C410004",
"patch=1,EE,0015FD44,word,242F0002",
"patch=1,EE,0015FD48,word,01E2C004",
"patch=1,EE,0015FD4C,word,00017900",
"patch=1,EE,0015FD50,word,030FC023",
"patch=1,EE,0015FD54,word,05A10003",
"patch=1,EE,0015FD58,word,240F0002",
"patch=1,EE,0015FD5C,word,002F7804",
"patch=1,EE,0015FD60,word,030FC021",
"patch=1,EE,0015FD64,word,0018C400",
"patch=1,EE,0015FD68,word,3C034000",
"patch=1,EE,0015FD6C,word,00781825",
"patch=1,EE,0015FD70,word,0003183C",
"patch=1,EE,0015FD74,word,10000002",
"patch=1,EE,0015FD78,word,FDC30000",
"patch=1,EE,0015FD7C,word,FDC40000",
"patch=1,EE,0015FD8C,word,1460FFE4",
"patch=1,EE,00136124,word,3C020187",
"patch=1,EE,00136128,word,2442AED0",
"patch=1,EE,0013612C,word,00464021",
"patch=1,EE,00136130,word,8D090000",
"patch=1,EE,00136134,word,312201FC",
"patch=1,EE,00136138,word,01224826",
"patch=1,EE,0013613C,word,0520000B",
"patch=1,EE,00136140,word,00000000",
"patch=1,EE,00136144,word,10400005",
"patch=1,EE,00136148,word,24030100",
"patch=1,EE,0013614C,word,10430005",
"patch=1,EE,00136150,word,3C038000",
"patch=1,EE,00136154,word,10000008",
"patch=1,EE,00136158,word,01234825",
"patch=1,EE,0013615C,word,10000006",
"patch=1,EE,00136160,word,24020004",
"patch=1,EE,00136164,word,10000004",
"patch=1,EE,00136168,word,0000102D",
"patch=1,EE,0013616C,word,3C038000",
"patch=1,EE,00136170,word,01234826",
"patch=1,EE,00136174,word,00021040",
"patch=1,EE,00136178,word,01224825",
"patch=1,EE,0013617C,word,AD090000",
"patch=1,EE,00136180,word,70401804",
"patch=1,EE,00136184,word,2401001E",
"patch=1,EE,00136188,word,00231823",
"patch=1,EE,0013618C,word,00031840",
"patch=1,EE,00136190,word,3C010003",
"patch=1,EE,00136194,word,3421E790",
"patch=1,EE,00136198,word,00611806",
"patch=1,EE,0013619C,word,30630003",
"patch=1,EE,001361A0,word,10000015",
"patch=1,EE,001361A4,word,ACA30000",
"patch=1,EE,001361A8,word,00000000",
"patch=1,EE,001361AC,word,00000000",
"patch=1,EE,00139944,word,306201FC",
"patch=1,EE,00139948,word,70401804",
"patch=1,EE,0013994C,word,2401001E",
"patch=1,EE,00139950,word,00231823",
"patch=1,EE,00139954,word,00031840",
"patch=1,EE,00139958,word,3C010003",
"patch=1,EE,0013995C,word,3421E790",
"patch=1,EE,00139960,word,00611806",
"patch=1,EE,00139964,word,03E00008",
"patch=1,EE,00139968,word,30620003"
]
},
{
"name": "Judge Timing Adjust",
"id": "jtime",
"lines": [
"author=Claude",
"description=判定タイミング調整。最後の行の下4桁(XXXX)が調整値で、1単位=4ms(16ビット符号付き)。0000=調整なし／FFFF=-4ms／FFFE=-8ms／FFFD=-12ms／FFFC=-16ms／FFFA=-24ms／FFF8=-32ms／0001=+4ms／0002=+8ms／0004=+16ms／0008=+32ms。マイナス=判定ラインが遅くなる(遅めに押してもジャスト)、プラス=判定ラインが早くなる。0x165404の daddu a1,s0,zero を addiu a1,s0,調整値 に置換(判定処理に渡す時刻だけをずらすので譜面表示と音はそのまま)。上4桁(2605)は変更しないこと。",
"patch=1,EE,00165404,word,2605FFF8"
]
},
{
"name": "COOL Judge in All Modes",
"id": "coolall",
"lines": [
"author=Claude",
"description=全モードでCOOL判定を有効化(GREAT範囲の中心±4でCOOL)し、スコア計算をCOOLありモードと同じ式にする。COOLのゲージ増加量はGREATと同じ(COOLありモードは従来どおり0)。オートプレイ/デモもCOOLになる。画面下のカウンターにもCOOLを表示する(モード5を除く)。",
"// 0x164DC0: COOL判定のモード条件を常に成立",
"// 0x165298: オートプレイのCOOL条件を常に成立",
"// 0x164924: スコア加算を全モードでCOOLありモードの式に(COOL=1000000/GREAT=500000/GOOD=100000)",
"// 0x165A8C: スコア満点を全モードでCOOLありモードの式に(ノーツ数x10)",
"// 0x163B3C: COOL時のゲージ増減にGREATの値を使う",
"// 0x14C378/0x14C394/0x14C414: 画面下の背景を常にCOOL付きの画像に(FREE=E60000、それ以外=E80000、モード5は対象外)",
"// 0x14BA38/0x14BA40: 右下の表示部品をCOOL付き背景に合う形で作成(モード5は対象外)",
"// 0x140588-0x14059C/0x1405A8-0x1405BC/0x14060C: リザルト画面の初期化を通常版(0x143750)からCOOL付き版(0x140F30)に差し替え(バトルは対象外)",
"// 0x140724/0x140740: リザルト画像の読み込みも通常版(0x144000, アーカイブD7)からCOOL付き版(0x141780, アーカイブD8)に差し替え(初期化だけ差し替えると画像が無く崩れる)",
"// 0x141028: フリートレーニング(0x186AEE0=4)ではCOOL付きリザルトの背景をフリートレーニング用(D80027)にする",
"patch=1,EE,00164DC0,word,1000000D",
"patch=1,EE,00165298,word,1000000C",
"patch=1,EE,00164924,word,1000000D",
"patch=1,EE,00165A8C,word,1000000C",
"patch=1,EE,00163B3C,word,24040000",
"patch=1,EE,0014BA38,word,0C063E28",
"patch=1,EE,0014BA40,word,1040000B",
"patch=1,EE,0014C378,word,34500000",
"patch=1,EE,0014C394,word,10000004",
"patch=1,EE,0014C414,word,34500000",
"patch=1,EE,0014058C,word,3C040187",
"patch=1,EE,00140590,word,8C25AEE4",
"patch=1,EE,00140594,word,0C0503CC",
"patch=1,EE,00140598,word,2484AF34",
"patch=1,EE,0014059C,word,00000000",
"patch=1,EE,001405AC,word,3C040187",
"patch=1,EE,001405B0,word,8C25AEE4",
"patch=1,EE,001405B4,word,0C0503CC",
"patch=1,EE,001405B8,word,2484AF34",
"patch=1,EE,001405BC,word,00000000",
"patch=1,EE,0014060C,word,00000000",
"patch=1,EE,00140724,word,0C0505E0",
"patch=1,EE,00140740,word,00000000",
"patch=1,EE,00141028,word,00000000"
]
},
{
"name": "Score Formula (current pop'n)",
"id": "score",
"lines": [
"author=Claude",
"description=COOLありモードのスコア式を現行ポップンの式に変更: スコア=100000×(COOL×1.0+GREAT×0.7+GOOD×0.4)÷ポップ君総数(小数点以下切り捨て)。全モードに適用するには[COOL Judge in All Modes]も有効にする。",
"// 0x1649A4-0x1649A8: GREATの加算値 500000 → 700000",
"// 0x1649D4-0x1649D8: GOODの加算値 100000 → 400000",
"patch=1,EE,001649A4,word,3C02000A",
"patch=1,EE,001649A8,word,3442AE60",
"patch=1,EE,001649D4,word,3C020006",
"patch=1,EE,001649D8,word,34421A80"
]
},
{
"name": "No FEVER at Gauge MAX",
"id": "nofever",
"lines": [
"author=Claude",
"description=ゲージMAX時(および一部モードのコンボ99以上)にGREATがFEVER表示になるのを無効化し、常に通常のGREATとして表示する(スコアは元からGREATと同じ扱いなので変化なし)。",
"// 0x163BA0: 通常GREAT処理のFEVER分岐を常に通常GREAT側へ",
"// 0x1A3B98: イベントコード11の処理のFEVER分岐を常に通常GREAT側へ",
"patch=1,EE,00163BA0,word,1000000B",
"patch=1,EE,001A3B98,word,1000000B"
]
},
{
"name": "Key Beam Length",
"id": "keybeam",
"lines": [
"author=Claude",
"description=キービームの長さを変更する。下端(判定ライン側)は固定のまま上に向かって縮み、グラデーションも縮小される。「長さ」と書いた1行の値(末尾8桁)を下の表の値に書き換えること。初期値は50%。",
"// 長さの値(元の長さ=100%、ビームの高さは元257px)",
"//     0% = 00000000 (  0px)",
"//    10% = 0000000A ( 25px)",
"//    20% = 00000014 ( 51px)",
"//    30% = 0000001E ( 77px)",
"//    40% = 00000028 (102px)",
"//    50% = 00000032 (128px)",
"//    60% = 0000003C (154px)",
"//    70% = 00000046 (179px)",
"//    80% = 00000050 (205px)",
"//    90% = 0000005A (231px)",
"//   100% = 00000064 (257px)",
"// 仕組み: ビームはスプライトセット0のフレーム260-267(テクスチャ30x257/24x257)。スプライト描画関数(0x121150)の頂点Y計算の直前(0x1214F4)に",
"//   コードを差し込み、描画する矩形が 幅30or24・高さ257 のとき、高さの拡大率(t2)を「長さ」%倍し、下端が動かないよう上端Yを下げる。",
"//   差し込みコードは空きRAM 0x000FFE00 以降、長さの値は 0x000FFF04 に置く。",
"// 長さ(この1行だけ書き換える)",
"patch=1,EE,000FFF04,word,00000032",
"// ここから下は変更しない",
"patch=1,EE,001214F4,word,0803FF80",
"patch=1,EE,000FFE00,word,01063021",
"patch=1,EE,000FFE04,word,1940001E",
"patch=1,EE,000FFE08,word,00000000",
"patch=1,EE,000FFE0C,word,84F00006",
"patch=1,EE,000FFE10,word,24130101",
"patch=1,EE,000FFE14,word,1613001A",
"patch=1,EE,000FFE18,word,00000000",
"patch=1,EE,000FFE1C,word,84F20004",
"patch=1,EE,000FFE20,word,2413001E",
"patch=1,EE,000FFE24,word,12530004",
"patch=1,EE,000FFE28,word,00000000",
"patch=1,EE,000FFE2C,word,24130018",
"patch=1,EE,000FFE30,word,16530013",
"patch=1,EE,000FFE34,word,00000000",
"patch=1,EE,000FFE38,word,3C130010",
"patch=1,EE,000FFE3C,word,8E73FF04",
"patch=1,EE,000FFE40,word,84F00006",
"patch=1,EE,000FFE44,word,020A0018",
"patch=1,EE,000FFE48,word,00006012",
"patch=1,EE,000FFE4C,word,24140064",
"patch=1,EE,000FFE50,word,0194001A",
"patch=1,EE,000FFE54,word,00006012",
"patch=1,EE,000FFE58,word,01930018",
"patch=1,EE,000FFE5C,word,00008012",
"patch=1,EE,000FFE60,word,0214001A",
"patch=1,EE,000FFE64,word,00008012",
"patch=1,EE,000FFE68,word,01906023",
"patch=1,EE,000FFE6C,word,00CC3021",
"patch=1,EE,000FFE70,word,01530018",
"patch=1,EE,000FFE74,word,00005012",
"patch=1,EE,000FFE78,word,0154001A",
"patch=1,EE,000FFE7C,word,00005012",
"patch=1,EE,000FFE80,word,0804853F",
"patch=1,EE,000FFE84,word,00000000"
]
},
{
"name": "Lane Brightness",
"id": "lane",
"lines": [
"comment=Darken the key lane background. Rewrite ONLY the value at 000FFA00 (hex, 00-64):",
"comment=  100%=00000064 (original)  90%=0000005A  80%=00000050  70%=00000046  60%=0000003C",
"comment=   50%=00000032  40%=00000028  30%=0000001E  20%=00000014  10%=0000000A  0%=00000000 (black)",
"comment=Default is 70%. Only the lane background is affected (not notes/beam).",
"patch=1,EE,000FFA00,word,0000001E",
"patch=1,EE,001215F0,word,0803FEC0",
"patch=1,EE,000FFB00,word,ADC000CC",
"patch=1,EE,000FFB04,word,8DC80090",
"patch=1,EE,000FFB08,word,8DC90094",
"patch=1,EE,000FFB0C,word,8DCA00C0",
"patch=1,EE,000FFB10,word,8DCB00C4",
"patch=1,EE,000FFB14,word,340C77F0",
"patch=1,EE,000FFB18,word,010C602B",
"patch=1,EE,000FFB1C,word,1580003B",
"patch=1,EE,000FFB20,word,00000000",
"patch=1,EE,000FFB24,word,340C6FF0",
"patch=1,EE,000FFB28,word,012C602B",
"patch=1,EE,000FFB2C,word,15800037",
"patch=1,EE,000FFB30,word,00000000",
"patch=1,EE,000FFB34,word,340C87A1",
"patch=1,EE,000FFB38,word,014C602B",
"patch=1,EE,000FFB3C,word,11800033",
"patch=1,EE,000FFB40,word,00000000",
"patch=1,EE,000FFB44,word,340C83D1",
"patch=1,EE,000FFB48,word,016C602B",
"patch=1,EE,000FFB4C,word,1180002F",
"patch=1,EE,000FFB50,word,00000000",
"patch=1,EE,000FFB54,word,01487823",
"patch=1,EE,000FFB58,word,2DEC0F80",
"patch=1,EE,000FFB5C,word,1580002B",
"patch=1,EE,000FFB60,word,00000000",
"patch=1,EE,000FFB64,word,2DEC0F81",
"patch=1,EE,000FFB68,word,11800028",
"patch=1,EE,000FFB6C,word,00000000",
"patch=1,EE,000FFB70,word,3C0C0010",
"patch=1,EE,000FFB74,word,8D8CFA00",
"patch=1,EE,000FFB78,word,240D0064",
"patch=1,EE,000FFB7C,word,8DC80080",
"patch=1,EE,000FFB80,word,010C0018",
"patch=1,EE,000FFB84,word,00004012",
"patch=1,EE,000FFB88,word,010D001A",
"patch=1,EE,000FFB8C,word,00004012",
"patch=1,EE,000FFB90,word,ADC80080",
"patch=1,EE,000FFB94,word,8DC80084",
"patch=1,EE,000FFB98,word,010C0018",
"patch=1,EE,000FFB9C,word,00004012",
"patch=1,EE,000FFBA0,word,010D001A",
"patch=1,EE,000FFBA4,word,00004012",
"patch=1,EE,000FFBA8,word,ADC80084",
"patch=1,EE,000FFBAC,word,8DC80088",
"patch=1,EE,000FFBB0,word,010C0018",
"patch=1,EE,000FFBB4,word,00004012",
"patch=1,EE,000FFBB8,word,010D001A",
"patch=1,EE,000FFBBC,word,00004012",
"patch=1,EE,000FFBC0,word,ADC80088",
"patch=1,EE,000FFBC4,word,8DC800B0",
"patch=1,EE,000FFBC8,word,010C0018",
"patch=1,EE,000FFBCC,word,00004012",
"patch=1,EE,000FFBD0,word,010D001A",
"patch=1,EE,000FFBD4,word,00004012",
"patch=1,EE,000FFBD8,word,ADC800B0",
"patch=1,EE,000FFBDC,word,8DC800B4",
"patch=1,EE,000FFBE0,word,010C0018",
"patch=1,EE,000FFBE4,word,00004012",
"patch=1,EE,000FFBE8,word,010D001A",
"patch=1,EE,000FFBEC,word,00004012",
"patch=1,EE,000FFBF0,word,ADC800B4",
"patch=1,EE,000FFBF4,word,8DC800B8",
"patch=1,EE,000FFBF8,word,010C0018",
"patch=1,EE,000FFBFC,word,00004012",
"patch=1,EE,000FFC00,word,010D001A",
"patch=1,EE,000FFC04,word,00004012",
"patch=1,EE,000FFC08,word,ADC800B8",
"patch=1,EE,000FFC0C,word,0804857D",
"patch=1,EE,000FFC10,word,00000000"
]
},
{
"name": "COOL Window 25ms",
"id": "coolwin",
"lines": [
"author=Claude",
"description=COOL判定の幅を±16ms(内部値±4)から現行ポップンの±25ms(内部値±6)に広げる。判定結果を決める処理の中で「時間差が-4以上かつ4以下ならCOOL」と比較している即値(-4と5)を(-6と7)に書き換えるだけで、GREAT以下の判定幅とスコア式は変えない。",
"// 内部の時間単位は1/240秒(約4.17ms)。COOL ±4=±16.7ms → ±6=±25.0ms。",
"// このタイトルのGREAT幅は内部値±12(約±50.0ms)なので、COOL ±6はGREATの内側に収まる。",
"// 幅を変えたい場合: 「-4」の行の末尾4桁を(-N)の16ビット値、「5」の行の末尾4桁を(N+1)に書き換える。",
"//   N=4(元)  FFFC / 0005    N=5  FFFB / 0006    N=6(25ms)  FFFA / 0007    N=7  FFF9 / 0008",
"// 「-4」の行は slti(時間差 < -N)、「5」の行は slti(時間差 < N+1)。「-4」の行が2つあるタイトルは、分岐の遅延スロットに入った同じ比較の複製(両方書き換える)。",
"patch=1,EE,00164DC4,word,2A42FFFA",
"patch=1,EE,00164DF4,word,2A42FFFA",
"patch=1,EE,00164DFC,word,2A410007"
]
},
{
"name": "480p Test (experimental)",
"id": "p480",
"lines": [
"author=Claude",
"comment=実験用。起動時にゲームを最初から起動すること（ステートのロードでは反映されない）。sceGsResetGraph を 480i→480p(inter=0, omode=0x50, ffmd=1) に変更し、480i のフィールド描画用の SCANMSK を常に 0 にする。さらに描画・表示を FBP 0 の1面に戻す（ロード中の真っ暗対策）。512幅のまま出力するため、PCSX2 側でアスペクト比を 4:3 にして使う。",
"patch=1,EE,001256E0,word,24050000",
"patch=1,EE,001256E4,word,24060050",
"patch=1,EE,001256EC,word,24070001",
"patch=1,EE,00124A28,word,24020000",
"patch=1,EE,001B3F90,word,00000000",
"patch=1,EE,001B4010,word,00000000",
"patch=1,EE,0012570C,word,0C03FDE0",
"patch=1,EE,000FF780,word,27BDFFF0",
"patch=1,EE,000FF784,word,FFBF0000",
"patch=1,EE,000FF788,word,0C04038A",
"patch=1,EE,000FF78C,word,00000000",
"patch=1,EE,000FF790,word,3C0800C3",
"patch=1,EE,000FF794,word,25083E50",
"patch=1,EE,000FF798,word,3C090208",
"patch=1,EE,000FF79C,word,AD090060",
"patch=1,EE,000FF7A0,word,AD090150",
"patch=1,EE,000FF7A4,word,3C090001",
"patch=1,EE,000FF7A8,word,35291000",
"patch=1,EE,000FF7AC,word,AD090010",
"patch=1,EE,000FF7B0,word,AD090038",
"patch=1,EE,000FF7B4,word,DFBF0000",
"patch=1,EE,000FF7B8,word,03E00008",
"patch=1,EE,000FF7BC,word,27BD0010"
]
},
{
"name": "Bar Lines OFF",
"id": "barline",
"lines": [
"author=Claude",
"comment=フリートレーニング等で表示される小節線（レーン幅いっぱいの横線）を非表示にする。描画関数 0x1491C0 を即 return させるだけ。A/Bリピート地点のマーカー(0x149240)は残る。",
"patch=1,EE,001491C0,word,03E00008",
"patch=1,EE,001491C4,word,00000000"
]
}
]
},
"SLPM-65508_DFBAFDE3": {
"gametitle": "gametitle=pop'n music 9 (CRC DFBAFDE3)",
"sections": [
{
"name": "HiSpeed x2-x8 with .5 steps (to x7.5)",
"id": "hispeed",
"lines": [
"author=Claude",
"comment=OFF→2→2.5→…→7.5→8→OFF。各段階の実速度はデフォルト値の1.2倍（x2=2.4…x8=9.6）。.5は値の最上位ビットで管理",
"patch=1,EE,00151D7C,word,308301FC",
"patch=1,EE,00151D80,word,1060001B",
"patch=1,EE,00151D84,word,00000000",
"patch=1,EE,00151D88,word,70601004",
"patch=1,EE,00151D8C,word,2403001E",
"patch=1,EE,00151D90,word,00621823",
"patch=1,EE,00151D94,word,00031840",
"patch=1,EE,00151D98,word,000417C2",
"patch=1,EE,00151D9C,word,00621821",
"patch=1,EE,00151DA0,word,44830000",
"patch=1,EE,00151DA4,word,46800020",
"patch=1,EE,00151DA8,word,3C023F19",
"patch=1,EE,00151DAC,word,3442999A",
"patch=1,EE,00151DB0,word,44820800",
"patch=1,EE,00151DB4,word,46010002",
"patch=1,EE,00151DB8,word,44020000",
"patch=1,EE,00151DBC,word,00021DC2",
"patch=1,EE,00151DC0,word,24630380",
"patch=1,EE,00151DC4,word,00031D00",
"patch=1,EE,00151DC8,word,00021240",
"patch=1,EE,00151DCC,word,00021302",
"patch=1,EE,00151DD0,word,00621825",
"patch=1,EE,00151DD4,word,10000012",
"patch=1,EE,00151DD8,word,0003183C",
"patch=1,EE,00151DDC,word,00000000",
"patch=1,EE,00151DE0,word,00000000",
"patch=1,EE,00151DE4,word,00000000",
"patch=1,EE,00151DE8,word,00000000",
"patch=1,EE,00151DEC,word,00000000",
"patch=1,EE,00165CF4,word,FFBF0010",
"patch=1,EE,00165CF8,word,7FB00000",
"patch=1,EE,00165CFC,word,308201FC",
"patch=1,EE,00165D00,word,00828026",
"patch=1,EE,00165D04,word,0600000C",
"patch=1,EE,00165D08,word,00000000",
"patch=1,EE,00165D0C,word,10400006",
"patch=1,EE,00165D10,word,24010100",
"patch=1,EE,00165D14,word,10410006",
"patch=1,EE,00165D18,word,00000000",
"patch=1,EE,00165D1C,word,3C018000",
"patch=1,EE,00165D20,word,10000008",
"patch=1,EE,00165D24,word,02018025",
"patch=1,EE,00165D28,word,10000006",
"patch=1,EE,00165D2C,word,24020004",
"patch=1,EE,00165D30,word,10000004",
"patch=1,EE,00165D34,word,0000102D",
"patch=1,EE,00165D38,word,3C018000",
"patch=1,EE,00165D3C,word,02018026",
"patch=1,EE,00165D40,word,00021040",
"patch=1,EE,00165D44,word,1000001E",
"patch=1,EE,00165D48,word,02028025"
]
},
{
"name": "Judge Timing Adjust",
"id": "jtime",
"lines": [
"author=Claude",
"description=判定タイミング調整。最後の行の下4桁(XXXX)が調整値で、1単位=4ms(16ビット符号付き)。0000=調整なし／FFFF=-4ms／FFFE=-8ms／FFFD=-12ms／FFFC=-16ms／FFFA=-24ms／FFF8=-32ms／0001=+4ms／0002=+8ms／0004=+16ms／0008=+32ms。マイナス=判定ラインが遅くなる(遅めに押してもジャスト)、プラス=判定ラインが早くなる。0x159D50の daddu a1,s1,zero を addiu a1,s1,調整値 に置換(判定処理に渡す時刻だけをずらすので譜面表示と音はそのまま)。",
"patch=1,EE,00159D50,word,2625FFF8"
]
},
{
"name": "COOL Judge in All Modes",
"id": "coolall",
"lines": [
"author=Claude",
"description=全モードでCOOL判定を有効化(GREAT範囲の中心±4でCOOL)し、スコア計算をEXPERTと同じ式にする。COOLのないモードではCOOLのゲージ増加量をGREATと同じにする。オートプレイ/デモもCOOLになる。画面下のカウンターにもCOOLを表示する。",
"// 0x1597DC: COOL判定のモード条件を常に成立",
"// 0x159C3C: オートプレイのCOOL条件を常に成立",
"// 0x15922C: スコア加算を全モードでEXPERTの式に(COOL=1000000/GREAT=500000/GOOD=100000)",
"// 0x15A230: スコア満点を全モードでEXPERTの式に(ノーツ数x10)",
"// 0x156D60-0x156D8C: 非COOLモードのゲージ初期化でCOOLの増加量=GREATの増加量",
"// 0x153294: 曲開始時のHUD COOL表示フラグを常にON(画面下のカウンターにCOOLを表示)",
"// 0x136848/0x137210/0x137660/0x156618/0x1564D0: リザルト画面の初期化を通常版(0x18B500)からCOOL付き版(0x18D9E0, EXPERT等と同じ)に差し替え(バトルは対象外)",
"patch=1,EE,00156D60,word,0C04E238",
"patch=1,EE,00156D64,word,00000000",
"patch=1,EE,00156D68,word,14400004",
"patch=1,EE,00156D6C,word,3C010194",
"patch=1,EE,00156D70,word,8423C468",
"patch=1,EE,00156D74,word,10000006",
"patch=1,EE,00156D78,word,A423C472",
"patch=1,EE,00156D7C,word,2403FFFF",
"patch=1,EE,00156D80,word,A420C46A",
"patch=1,EE,00156D84,word,A420C468",
"patch=1,EE,00156D88,word,A423C46E",
"patch=1,EE,00156D8C,word,A423C46C",
"patch=1,EE,001597DC,word,1000000A",
"patch=1,EE,00159C3C,word,1000000A",
"patch=1,EE,00153294,word,1000000A",
"patch=1,EE,0015922C,word,1000000A",
"patch=1,EE,0015A230,word,1000000B",
"patch=1,EE,00136848,word,0C063678",
"patch=1,EE,00137210,word,0C063678",
"patch=1,EE,00137660,word,0C063678",
"patch=1,EE,00156618,word,0C063678",
"patch=1,EE,001564D0,word,0C063678"
]
},
{
"name": "Score Formula (current pop'n)",
"id": "score",
"lines": [
"author=Claude",
"description=EXPERTのスコア式を現行ポップンの式に変更: スコア=100000×(COOL×1.0+GREAT×0.7+GOOD×0.4)÷ポップ君総数(小数点以下切り捨て)。全モードに適用するには[COOL Judge in All Modes]も有効にする。",
"// 0x1592A0-0x1592A4: GREATの加算値 500000 → 700000",
"// 0x1592D4-0x1592D8: GOODの加算値 100000 → 400000",
"patch=1,EE,001592A0,word,3C02000A",
"patch=1,EE,001592A4,word,3442AE60",
"patch=1,EE,001592D4,word,3C020006",
"patch=1,EE,001592D8,word,34421A80"
]
},
{
"name": "No FEVER at Gauge MAX",
"id": "nofever",
"lines": [
"author=Claude",
"description=ゲージMAX時(および一部モードのコンボ99以上)にGREATがFEVER表示になるのを無効化し、常に通常のGREATとして表示する(スコアは元からGREATと同じ扱いなので変化なし)。",
"// 0x1583A0: GREAT処理のFEVER分岐を常に通常GREAT側へ",
"patch=1,EE,001583A0,word,10000009"
]
},
{
"name": "Key Beam Length",
"id": "keybeam",
"lines": [
"author=Claude",
"description=キービームの長さを変更する。下端(判定ライン側)は固定のまま上に向かって縮み、グラデーションも縮小される。「長さ」と書いた1行の値(末尾8桁)を下の表の値に書き換えること。初期値は50%。",
"// 長さの値(元の長さ=100%、画面上のビームの高さは元約330px)",
"//     0% = 00000000 (約  0px)",
"//    10% = 0000000A (約 32px)",
"//    20% = 00000014 (約 65px)",
"//    30% = 0000001E (約 98px)",
"//    40% = 00000028 (約131px)",
"//    50% = 00000032 (約164px)",
"//    60% = 0000003C (約197px)",
"//    70% = 00000046 (約230px)",
"//    80% = 00000050 (約263px)",
"//    90% = 0000005A (約296px)",
"//   100% = 00000064 (約329px)",
"// 仕組み: ビームはテクスチャ30x308/24x308のスプライト。スプライト描画関数(0x124F50)の上端Y計算の直後(0x125190)に",
"//   コードを差し込み、描画する矩形が 幅30or24・高さ308 のとき、高さの拡大率(t2)を「長さ」%倍し、下端が動かないよう上端Yを下げる。",
"//   差し込みコードは空きRAM 0x000FFE00 以降、長さの値は 0x000FFF04 に置く。",
"// 長さ(この1行だけ書き換える)",
"patch=1,EE,000FFF04,word,00000032",
"// ここから下は変更しない",
"patch=1,EE,00125190,word,0803FF80",
"patch=1,EE,000FFE00,word,1940001F",
"patch=1,EE,000FFE04,word,00000000",
"patch=1,EE,000FFE08,word,24050134",
"patch=1,EE,000FFE0C,word,14E5001C",
"patch=1,EE,000FFE10,word,00000000",
"patch=1,EE,000FFE14,word,2405001E",
"patch=1,EE,000FFE18,word,11850004",
"patch=1,EE,000FFE1C,word,00000000",
"patch=1,EE,000FFE20,word,24050018",
"patch=1,EE,000FFE24,word,15850016",
"patch=1,EE,000FFE28,word,00000000",
"patch=1,EE,000FFE2C,word,3C060010",
"patch=1,EE,000FFE30,word,8CC6FF04",
"patch=1,EE,000FFE34,word,00EA0018",
"patch=1,EE,000FFE38,word,00002812",
"patch=1,EE,000FFE3C,word,24030064",
"patch=1,EE,000FFE40,word,00A3001A",
"patch=1,EE,000FFE44,word,00002812",
"patch=1,EE,000FFE48,word,01460018",
"patch=1,EE,000FFE4C,word,00005012",
"patch=1,EE,000FFE50,word,0143001A",
"patch=1,EE,000FFE54,word,00005012",
"patch=1,EE,000FFE58,word,00EA0018",
"patch=1,EE,000FFE5C,word,00003012",
"patch=1,EE,000FFE60,word,00C3001A",
"patch=1,EE,000FFE64,word,00003012",
"patch=1,EE,000FFE68,word,00A62823",
"patch=1,EE,000FFE6C,word,44850000",
"patch=1,EE,000FFE70,word,00000000",
"patch=1,EE,000FFE74,word,46800020",
"patch=1,EE,000FFE78,word,00000000",
"patch=1,EE,000FFE7C,word,46003180",
"patch=1,EE,000FFE80,word,3C0351EB",
"patch=1,EE,000FFE84,word,08049466",
"patch=1,EE,000FFE88,word,001431C0"
]
},
{
"name": "Lane Brightness",
"id": "lane",
"lines": [
"comment=Darken the key lane background. Rewrite ONLY the value at 000FFA00 (hex, 00-64):",
"comment=  100%=00000064 (original)  90%=0000005A  80%=00000050  70%=00000046  60%=0000003C",
"comment=   50%=00000032  40%=00000028  30%=0000001E  20%=00000014  10%=0000000A  0%=00000000 (black)",
"comment=Default is 70%. Only the lane background is affected (not notes/beam).",
"patch=1,EE,000FFA00,word,0000000A",
"patch=1,EE,001257C4,word,0803FEC0",
"patch=1,EE,000FFB00,word,AF2000CC",
"patch=1,EE,000FFB04,word,8F280090",
"patch=1,EE,000FFB08,word,8F290094",
"patch=1,EE,000FFB0C,word,8F2A00C0",
"patch=1,EE,000FFB10,word,8F2B00C4",
"patch=1,EE,000FFB14,word,340C77F0",
"patch=1,EE,000FFB18,word,010C602B",
"patch=1,EE,000FFB1C,word,1580003F",
"patch=1,EE,000FFB20,word,00000000",
"patch=1,EE,000FFB24,word,340C71D0",
"patch=1,EE,000FFB28,word,012C602B",
"patch=1,EE,000FFB2C,word,1580003B",
"patch=1,EE,000FFB30,word,00000000",
"patch=1,EE,000FFB34,word,340C8801",
"patch=1,EE,000FFB38,word,014C602B",
"patch=1,EE,000FFB3C,word,11800037",
"patch=1,EE,000FFB40,word,00000000",
"patch=1,EE,000FFB44,word,340C8A01",
"patch=1,EE,000FFB48,word,016C602B",
"patch=1,EE,000FFB4C,word,11800033",
"patch=1,EE,000FFB50,word,00000000",
"patch=1,EE,000FFB54,word,01487823",
"patch=1,EE,000FFB58,word,2DEC1000",
"patch=1,EE,000FFB5C,word,1580002F",
"patch=1,EE,000FFB60,word,00000000",
"patch=1,EE,000FFB64,word,2DEC1001",
"patch=1,EE,000FFB68,word,1180002C",
"patch=1,EE,000FFB6C,word,00000000",
"patch=1,EE,000FFB70,word,0169C023",
"patch=1,EE,000FFB74,word,2F0C1500",
"patch=1,EE,000FFB78,word,15800028",
"patch=1,EE,000FFB7C,word,00000000",
"patch=1,EE,000FFB80,word,3C0C0010",
"patch=1,EE,000FFB84,word,8D8CFA00",
"patch=1,EE,000FFB88,word,240D0064",
"patch=1,EE,000FFB8C,word,8F280080",
"patch=1,EE,000FFB90,word,010C0018",
"patch=1,EE,000FFB94,word,00004012",
"patch=1,EE,000FFB98,word,010D001A",
"patch=1,EE,000FFB9C,word,00004012",
"patch=1,EE,000FFBA0,word,AF280080",
"patch=1,EE,000FFBA4,word,8F280084",
"patch=1,EE,000FFBA8,word,010C0018",
"patch=1,EE,000FFBAC,word,00004012",
"patch=1,EE,000FFBB0,word,010D001A",
"patch=1,EE,000FFBB4,word,00004012",
"patch=1,EE,000FFBB8,word,AF280084",
"patch=1,EE,000FFBBC,word,8F280088",
"patch=1,EE,000FFBC0,word,010C0018",
"patch=1,EE,000FFBC4,word,00004012",
"patch=1,EE,000FFBC8,word,010D001A",
"patch=1,EE,000FFBCC,word,00004012",
"patch=1,EE,000FFBD0,word,AF280088",
"patch=1,EE,000FFBD4,word,8F2800B0",
"patch=1,EE,000FFBD8,word,010C0018",
"patch=1,EE,000FFBDC,word,00004012",
"patch=1,EE,000FFBE0,word,010D001A",
"patch=1,EE,000FFBE4,word,00004012",
"patch=1,EE,000FFBE8,word,AF2800B0",
"patch=1,EE,000FFBEC,word,8F2800B4",
"patch=1,EE,000FFBF0,word,010C0018",
"patch=1,EE,000FFBF4,word,00004012",
"patch=1,EE,000FFBF8,word,010D001A",
"patch=1,EE,000FFBFC,word,00004012",
"patch=1,EE,000FFC00,word,AF2800B4",
"patch=1,EE,000FFC04,word,8F2800B8",
"patch=1,EE,000FFC08,word,010C0018",
"patch=1,EE,000FFC0C,word,00004012",
"patch=1,EE,000FFC10,word,010D001A",
"patch=1,EE,000FFC14,word,00004012",
"patch=1,EE,000FFC18,word,AF2800B8",
"patch=1,EE,000FFC1C,word,080495F2",
"patch=1,EE,000FFC20,word,00000000"
]
},
{
"name": "COOL Window 25ms",
"id": "coolwin",
"lines": [
"author=Claude",
"description=COOL判定の幅を±16ms(内部値±4)から現行ポップンの±25ms(内部値±6)に広げる。判定結果を決める処理の中で「時間差が-4以上かつ4以下ならCOOL」と比較している即値(-4と5)を(-6と7)に書き換えるだけで、GREAT以下の判定幅とスコア式は変えない。",
"// 内部の時間単位は1/240秒(約4.17ms)。COOL ±4=±16.7ms → ±6=±25.0ms。",
"// このタイトルのGREAT幅は内部値±12(約±50.0ms)なので、COOL ±6はGREATの内側に収まる。",
"// 幅を変えたい場合: 「-4」の行の末尾4桁を(-N)の16ビット値、「5」の行の末尾4桁を(N+1)に書き換える。",
"//   N=4(元)  FFFC / 0005    N=5  FFFB / 0006    N=6(25ms)  FFFA / 0007    N=7  FFF9 / 0008",
"// 「-4」の行は slti(時間差 < -N)、「5」の行は slti(時間差 < N+1)。「-4」の行が2つあるタイトルは、分岐の遅延スロットに入った同じ比較の複製(両方書き換える)。",
"patch=1,EE,00159808,word,2A02FFFA",
"patch=1,EE,00159810,word,2A010007"
]
},
{
"name": "480p Test (experimental)",
"id": "p480",
"lines": [
"author=Claude",
"comment=実験用。起動時にゲームを最初から起動すること（ステートのロードでは反映されない）。sceGsResetGraph を 480i→480p(inter=0, omode=0x50, ffmd=1) に変更 し、毎フレームの DISPLAY 定数を 480p 用(DX=440 DY=35 MAGH=2倍 DW=1023 DH=447)にする。512幅のまま出力するため、PCSX2 側でアスペクト比を 4:3 にして使う。",
"patch=1,EE,0012A170,word,24050000",
"patch=1,EE,0012A174,word,24060050",
"patch=1,EE,0012A17C,word,24070001",
"patch=1,EE,0012AB28,word,3443F3FF",
"patch=1,EE,0012AB2C,word,3C020082",
"patch=1,EE,0012AB34,word,344331B8",
"patch=1,EE,0012AB38,word,344231B8"
]
}
]
},
"SLPM-65770_088871A6": {
"gametitle": "gametitle=pop'n music 10 (CRC 088871A6)",
"sections": [
{
"name": "HiSpeed x2-x8 with .5 steps + LOW",
"id": "hispeed",
"lines": [
"author=Claude",
"description=HiSpeed 2.0～8.0まで0.5刻みで設定可能。LOWモードも有効化。HiSpeedの倍率は0x139C60～0x139D0Cの値を差し替え。LOWモードは0x16DFA8～0x16DFBCの値を差し替え(HiSpeedと同じ倍率にする)。LOWモードの有効化は0x173F14のdaddu→addiu差し替えで判定処理に渡す時刻だけをずらすので譜面表示と音はそのまま。",
"patch=1,EE,00139C60,word,308841FC",
"patch=1,EE,00139C64,word,00884826",
"patch=1,EE,00139C68,word,3C0E0014",
"patch=1,EE,00139C6C,word,25CE9D10",
"patch=1,EE,00139C70,word,01C0502D",
"patch=1,EE,00139C74,word,0000582D",
"patch=1,EE,00139C78,word,954C0000",
"patch=1,EE,00139C7C,word,11880005",
"patch=1,EE,00139C80,word,256B0001",
"patch=1,EE,00139C84,word,296D000F",
"patch=1,EE,00139C88,word,15A0FFFB",
"patch=1,EE,00139C8C,word,254A0002",
"patch=1,EE,00139C90,word,240B0001",
"patch=1,EE,00139C94,word,240D000F",
"patch=1,EE,00139C98,word,156D0002",
"patch=1,EE,00139C9C,word,00000000",
"patch=1,EE,00139CA0,word,0000582D",
"patch=1,EE,00139CA4,word,000B5840",
"patch=1,EE,00139CA8,word,01CB7021",
"patch=1,EE,00139CAC,word,95CC0000",
"patch=1,EE,00139CB0,word,03E00008",
"patch=1,EE,00139CB4,word,012C1025",
"patch=1,EE,00139CB8,word,3082007C",
"patch=1,EE,00139CBC,word,00021082",
"patch=1,EE,00139CC0,word,3C010014",
"patch=1,EE,00139CC4,word,00220821",
"patch=1,EE,00139CC8,word,90229D30",
"patch=1,EE,00139CCC,word,1040000E",
"patch=1,EE,00139CD0,word,00045B42",
"patch=1,EE,00139CD4,word,316B0002",
"patch=1,EE,00139CD8,word,004B1021",
"patch=1,EE,00139CDC,word,00045942",
"patch=1,EE,00139CE0,word,316B0004",
"patch=1,EE,00139CE4,word,004B1021",
"patch=1,EE,00139CE8,word,284B0008",
"patch=1,EE,00139CEC,word,15600003",
"patch=1,EE,00139CF0,word,00025880",
"patch=1,EE,00139CF4,word,00025840",
"patch=1,EE,00139CF8,word,256B0010",
"patch=1,EE,00139CFC,word,256B3FF0",
"patch=1,EE,00139D00,word,03E00008",
"patch=1,EE,00139D04,word,000B143C",
"patch=1,EE,00139D08,word,03E00008",
"patch=1,EE,00139D0C,word,00000000",
"patch=1,EE,00139D10,word,00040000",
"patch=1,EE,00139D14,word,0008000C",
"patch=1,EE,00139D18,word,00100018",
"patch=1,EE,00139D1C,word,00500030",
"patch=1,EE,00139D20,word,00400070",
"patch=1,EE,00139D24,word,41400060",
"patch=1,EE,00139D28,word,01C04160",
"patch=1,EE,00139D2C,word,00000100",
"patch=1,EE,00139D30,word,05060400",
"patch=1,EE,00139D34,word,00070008",
"patch=1,EE,00139D38,word,00000000",
"patch=1,EE,00139D3C,word,00000009",
"patch=1,EE,00139D40,word,0000000C",
"patch=1,EE,00139D44,word,0000000A",
"patch=1,EE,00139D48,word,0000000D",
"patch=1,EE,00139D4C,word,0000000B",
"patch=1,EE,0016DFA8,word,0C04E72E",
"patch=1,EE,0016DFAC,word,00000000",
"patch=1,EE,0016DFB0,word,1040003F",
"patch=1,EE,0016DFB4,word,0040182D",
"patch=1,EE,0016DFB8,word,10000009",
"patch=1,EE,0016DFBC,word,00000000"
]
},
{
"name": "Judge Timing Adjust",
"id": "jtime",
"lines": [
"author=Claude",
"description=判定タイミング調整。最後の行の下4桁(XXXX)が調整値で、1単位=4ms(16ビット符号付き)。0000=調整なし／FFFF=-4ms／FFFE=-8ms／FFFD=-12ms／FFFC=-16ms／FFFA=-24ms／FFF8=-32ms／0001=+4ms／0002=+8ms／0004=+16ms／0008=+32ms。マイナス=判定ラインが遅くなる(遅めに押してもジャスト)、プラス=判定ラインが早くなる。0x173F14の daddu a1,s1,zero を addiu a1,s1,調整値 に置換(判定処理に渡す時刻だけをずらすので譜面表示と音はそのまま)。上4桁(2625)は変更しないこと。",
"patch=1,EE,00173F14,word,2625FFF8"
]
},
{
"name": "COOL Judge in All Modes",
"id": "coolall",
"lines": [
"author=Claude",
"description=全モードでCOOL判定を有効化(GREAT範囲の中心±4でCOOL)し、スコア計算をCOOLありモードと同じ式にする。COOLのゲージ増加量はGREATと同じ(ゲージの仕様と表示は各モードのまま)。オートプレイ/デモもCOOLになる。画面下のカウンター欄を全モードでCOOL付きにする。",
"// 0x173974: COOL判定のモード条件を常に成立",
"// 0x173D50: オートプレイのCOOL条件を常に成立",
"// 0x173398: スコア加算を全モードでCOOLありモードの式に(COOL=1000000/GREAT=500000/GOOD=100000)",
"// 0x174410: スコア満点を全モードでCOOLありモードの式に(ノーツ数x10)",
"// 0x172528: COOL時のゲージ増減にGREATの値を使う",
"// 0x17E50C: 画面下のカウンター数字をCOOL付きで更新",
"// 0x17BE08: 画面下のカウンター欄の画像をCOOL付きのスプライトに(同じテクスチャページ内)",
"// 0x204C60/64/68/74: リザルト画面の項目パネルをモード0/1/2/5(とトレーニング)でもCOOL付きのもの(EXPERT/トレーニングEXPERTと同じ)に(モード別ジャンプテーブルの差し替え。バトル(3)・モード7は対象外)",
"patch=1,EE,00172528,word,24040000",
"patch=1,EE,00173398,word,00000000",
"patch=1,EE,00173974,word,00000000",
"patch=1,EE,00173D50,word,10000039",
"patch=1,EE,00174410,word,00000000",
"patch=1,EE,0017BE08,word,00000000",
"patch=1,EE,0017E50C,word,00000000",
"patch=1,EE,00204C60,word,001B28AC",
"patch=1,EE,00204C64,word,001B28AC",
"patch=1,EE,00204C68,word,001B28AC",
"patch=1,EE,00204C74,word,001B28AC"
]
},
{
"name": "Score Formula (current pop'n)",
"id": "score",
"lines": [
"author=Claude",
"description=COOLありモードのスコア式を現行ポップンの式に変更: スコア=100000×(COOL×1.0+GREAT×0.7+GOOD×0.4)÷ポップ君総数(小数点以下切り捨て)。全モードに適用するには[COOL Judge in All Modes]も有効にする。",
"// 0x173554-0x173558: GREATの加算値 500000 → 700000",
"// 0x1733D4-0x1733D8: GOODの加算値 100000 → 400000",
"patch=1,EE,001733D4,word,3C020006",
"patch=1,EE,001733D8,word,34421A80",
"patch=1,EE,00173554,word,3C02000A",
"patch=1,EE,00173558,word,3442AE60"
]
},
{
"name": "No FEVER at Gauge MAX",
"id": "nofever",
"lines": [
"author=Claude",
"description=ゲージMAX時(および一部モードのコンボ99以上)にGREATがFEVER表示になるのを無効化し、常に通常のGREATとして表示する(スコアは元からGREATと同じ扱いなので変化なし)。",
"// 0x172584: FEVER判定の分岐を常に通常GREAT側へ",
"patch=1,EE,00172584,word,10000009"
]
},
{
"name": "PERFECT = GOOD 0 and BAD 0",
"id": "perfect",
"lines": [
"author=Claude",
"description=PERFECT(パーフェクト)の条件を「GOODとBADが0」に変更する(GREAT/COOLのみならPERFECT扱い)。COOL判定やスコア計算式の変更で満点にならない場合でもPERFECTになる。",
"// 0x152AF0/0x152EC8/0x1531B4/0x153E3C: PERFECT判定のスコア=100000条件を「スコア>0」に変更(GOOD=0かつBAD=0は元の条件のまま)",
"// 0x1B2C14/0x1B2C20: 記録用PERFECTフラグの条件をスコア=100000からGOOD=0に変更(BAD=0はフルコンボ条件で判定済み)",
"// 0x1B3650-0x1B365C: リザルトのPERFECT表示条件をスコア=100000からGOOD=0かつBAD=0に変更",
"patch=1,EE,00152AF0,word,1060000B",
"patch=1,EE,00152EC8,word,1080000B",
"patch=1,EE,001531B4,word,1080000B",
"patch=1,EE,00153E3C,word,1080000B",
"patch=1,EE,001B2C14,word,8E430014",
"patch=1,EE,001B2C20,word,1460FFDF",
"patch=1,EE,001B3650,word,8C830014",
"patch=1,EE,001B3654,word,8C820018",
"patch=1,EE,001B3658,word,00621825",
"patch=1,EE,001B365C,word,1060001C"
]
},
{
"name": "Key Beam Length",
"id": "keybeam",
"lines": [
"author=Claude",
"description=キービームの長さを変更する。下端(判定ライン側)は固定のまま上に向かって縮み、グラデーションも縮小される。「長さ」と書いた1行の値(末尾8桁)を下の表の値に書き換えること。初期値は50%。",
"// 長さの値(元の長さ=100%、画面上のビームの高さは元約308px)",
"//    0% = 00000000 (約  0px)",
"//   10% = 0000000A (約 31px)",
"//   20% = 00000014 (約 62px)",
"//   30% = 0000001E (約 92px)",
"//   40% = 00000028 (約123px)",
"//   50% = 00000032 (約154px)",
"//   60% = 0000003C (約185px)",
"//   70% = 00000046 (約216px)",
"//   80% = 00000050 (約246px)",
"//   90% = 0000005A (約277px)",
"//  100% = 00000064 (約308px)",
"// 仕組み: ビームはテクスチャ30x308/24x308のスプライト。スプライト描画関数(0x198040)の上端Y計算の直後(0x1981A0)に",
"//   コードを差し込み、描画する矩形が 幅30or24・高さ308 のとき、高さの拡大率(t2)を「長さ」%倍し、下端が動かないよう上端Yを下げる。",
"//   差し込みコードは空きRAM 0x000FFE00 以降、長さの値は 0x000FFF04 に置く。",
"// 長さ(この1行だけ書き換える)",
"patch=1,EE,000FFF04,word,00000032",
"// ここから下は変更しない",
"patch=1,EE,001981A0,word,0803FF80",
"patch=1,EE,000FFE00,word,1940001D",
"patch=1,EE,000FFE04,word,00000000",
"patch=1,EE,000FFE08,word,24050134",
"patch=1,EE,000FFE0C,word,1465001A",
"patch=1,EE,000FFE10,word,00000000",
"patch=1,EE,000FFE14,word,2405001E",
"patch=1,EE,000FFE18,word,11850004",
"patch=1,EE,000FFE1C,word,00000000",
"patch=1,EE,000FFE20,word,24050018",
"patch=1,EE,000FFE24,word,15850014",
"patch=1,EE,000FFE28,word,00000000",
"patch=1,EE,000FFE2C,word,3C0B0010",
"patch=1,EE,000FFE30,word,8D6BFF04",
"patch=1,EE,000FFE34,word,014B0018",
"patch=1,EE,000FFE38,word,00005812",
"patch=1,EE,000FFE3C,word,24050064",
"patch=1,EE,000FFE40,word,0165001A",
"patch=1,EE,000FFE44,word,00005812",
"patch=1,EE,000FFE48,word,014B2823",
"patch=1,EE,000FFE4C,word,00650018",
"patch=1,EE,000FFE50,word,00002812",
"patch=1,EE,000FFE54,word,01605021",
"patch=1,EE,000FFE58,word,240B0064",
"patch=1,EE,000FFE5C,word,00AB001A",
"patch=1,EE,000FFE60,word,00002812",
"patch=1,EE,000FFE64,word,44850000",
"patch=1,EE,000FFE68,word,00000000",
"patch=1,EE,000FFE6C,word,46800020",
"patch=1,EE,000FFE70,word,00000000",
"patch=1,EE,000FFE74,word,46004A40",
"patch=1,EE,000FFE78,word,3C0551EB",
"patch=1,EE,000FFE7C,word,0806606A",
"patch=1,EE,000FFE80,word,001331C0"
]
},
{
"name": "Lane Brightness",
"id": "lane",
"lines": [
"author=Claude",
"comment=Darken the key lane background. Rewrite ONLY the value at 000FFA00 (hex, 00-64):",
"comment=  100%=00000064 (original)  90%=0000005A  80%=00000050  70%=00000046  60%=0000003C",
"comment=   50%=00000032  40%=00000028  30%=0000001E  20%=00000014  10%=0000000A  0%=00000000 (black)",
"comment=Default is 70%. Only the lane background is affected (not notes/beam).",
"patch=1,EE,000FFA00,word,00000014",
"patch=1,EE,001987A8,word,0803FEC0",
"patch=1,EE,000FFB00,word,ADA000CC",
"patch=1,EE,000FFB04,word,8DA80090",
"patch=1,EE,000FFB08,word,8DA90094",
"patch=1,EE,000FFB0C,word,8DAA00C0",
"patch=1,EE,000FFB10,word,8DAB00C4",
"patch=1,EE,000FFB14,word,340C77F0",
"patch=1,EE,000FFB18,word,010C602B",
"patch=1,EE,000FFB1C,word,1580003F",
"patch=1,EE,000FFB20,word,00000000",
"patch=1,EE,000FFB24,word,340C71D0",
"patch=1,EE,000FFB28,word,012C602B",
"patch=1,EE,000FFB2C,word,1580003B",
"patch=1,EE,000FFB30,word,00000000",
"patch=1,EE,000FFB34,word,340C8801",
"patch=1,EE,000FFB38,word,014C602B",
"patch=1,EE,000FFB3C,word,11800037",
"patch=1,EE,000FFB40,word,00000000",
"patch=1,EE,000FFB44,word,340C8A01",
"patch=1,EE,000FFB48,word,016C602B",
"patch=1,EE,000FFB4C,word,11800033",
"patch=1,EE,000FFB50,word,00000000",
"patch=1,EE,000FFB54,word,01487823",
"patch=1,EE,000FFB58,word,2DEC1000",
"patch=1,EE,000FFB5C,word,1580002F",
"patch=1,EE,000FFB60,word,00000000",
"patch=1,EE,000FFB64,word,2DEC1001",
"patch=1,EE,000FFB68,word,1180002C",
"patch=1,EE,000FFB6C,word,00000000",
"patch=1,EE,000FFB70,word,0169C023",
"patch=1,EE,000FFB74,word,2F0C1600",
"patch=1,EE,000FFB78,word,15800028",
"patch=1,EE,000FFB7C,word,00000000",
"patch=1,EE,000FFB80,word,3C0C0010",
"patch=1,EE,000FFB84,word,8D8CFA00",
"patch=1,EE,000FFB88,word,240E0064",
"patch=1,EE,000FFB8C,word,8DA80080",
"patch=1,EE,000FFB90,word,010C0018",
"patch=1,EE,000FFB94,word,00004012",
"patch=1,EE,000FFB98,word,010E001A",
"patch=1,EE,000FFB9C,word,00004012",
"patch=1,EE,000FFBA0,word,ADA80080",
"patch=1,EE,000FFBA4,word,8DA80084",
"patch=1,EE,000FFBA8,word,010C0018",
"patch=1,EE,000FFBAC,word,00004012",
"patch=1,EE,000FFBB0,word,010E001A",
"patch=1,EE,000FFBB4,word,00004012",
"patch=1,EE,000FFBB8,word,ADA80084",
"patch=1,EE,000FFBBC,word,8DA80088",
"patch=1,EE,000FFBC0,word,010C0018",
"patch=1,EE,000FFBC4,word,00004012",
"patch=1,EE,000FFBC8,word,010E001A",
"patch=1,EE,000FFBCC,word,00004012",
"patch=1,EE,000FFBD0,word,ADA80088",
"patch=1,EE,000FFBD4,word,8DA800B0",
"patch=1,EE,000FFBD8,word,010C0018",
"patch=1,EE,000FFBDC,word,00004012",
"patch=1,EE,000FFBE0,word,010E001A",
"patch=1,EE,000FFBE4,word,00004012",
"patch=1,EE,000FFBE8,word,ADA800B0",
"patch=1,EE,000FFBEC,word,8DA800B4",
"patch=1,EE,000FFBF0,word,010C0018",
"patch=1,EE,000FFBF4,word,00004012",
"patch=1,EE,000FFBF8,word,010E001A",
"patch=1,EE,000FFBFC,word,00004012",
"patch=1,EE,000FFC00,word,ADA800B4",
"patch=1,EE,000FFC04,word,8DA800B8",
"patch=1,EE,000FFC08,word,010C0018",
"patch=1,EE,000FFC0C,word,00004012",
"patch=1,EE,000FFC10,word,010E001A",
"patch=1,EE,000FFC14,word,00004012",
"patch=1,EE,000FFC18,word,ADA800B8",
"patch=1,EE,000FFC1C,word,080661EB",
"patch=1,EE,000FFC20,word,00000000"
]
},
{
"name": "COOL Window 25ms",
"id": "coolwin",
"lines": [
"author=Claude",
"description=COOL判定の幅を±16ms(内部値±4)から現行ポップンの±25ms(内部値±6)に広げる。判定結果を決める処理の中で「時間差が-4以上かつ4以下ならCOOL」と比較している即値(-4と5)を(-6と7)に書き換えるだけで、GREAT以下の判定幅とスコア式は変えない。",
"// 内部の時間単位は1/240秒(約4.17ms)。COOL ±4=±16.7ms → ±6=±25.0ms。",
"// このタイトルのGREAT幅は内部値±12(約±50.0ms)なので、COOL ±6はGREATの内側に収まる。",
"// 幅を変えたい場合: 「-4」の行の末尾4桁を(-N)の16ビット値、「5」の行の末尾4桁を(N+1)に書き換える。",
"//   N=4(元)  FFFC / 0005    N=5  FFFB / 0006    N=6(25ms)  FFFA / 0007    N=7  FFF9 / 0008",
"// 「-4」の行は slti(時間差 < -N)、「5」の行は slti(時間差 < N+1)。「-4」の行が2つあるタイトルは、分岐の遅延スロットに入った同じ比較の複製(両方書き換える)。",
"patch=1,EE,0017397C,word,2A22FFFA",
"patch=1,EE,001739C4,word,2A22FFFA",
"patch=1,EE,00173988,word,2A210007"
]
},
{
"name": "480p Test (experimental)",
"id": "p480",
"lines": [
"author=Claude",
"comment=実験用。起動時にゲームを最初から起動すること（ステートのロードでは反映されない）。sceGsResetGraph を 480i→480p(inter=0, omode=0x50, ffmd=1) に変更 し、毎フレームの DISPLAY 定数を 480p 用(DX=440 DY=35 MAGH=2倍 DW=1023 DH=447)にする。512幅のまま出力するため、PCSX2 側でアスペクト比を 4:3 にして使う。",
"patch=1,EE,001A13A0,word,24050000",
"patch=1,EE,001A13A4,word,24060050",
"patch=1,EE,001A13AC,word,24070001",
"patch=1,EE,001A1D94,word,3463F3FF",
"patch=1,EE,001A1DA4,word,3C030082",
"patch=1,EE,001A1DAC,word,346431B8",
"patch=1,EE,001A1DB0,word,346331B8"
]
}
]
},
"SLPM-66065_47F66D02": {
"gametitle": "gametitle=pop'n music 11 (CRC 47F66D02)",
"sections": [
{
"name": "HiSpeed x2-x10 with .5 steps",
"id": "hispeed",
"lines": [
"author=Claude",
"comment=OFF→2→2.5→…→9.5→10→OFF（左右両方向対応）。全オプションの進む/戻るボタンを入れ替え。.5は元の段階の表示、x7〜x10は x2/x2/x3/x3/x4/x4/x5 の表示",
"patch=1,EE,0018F0D0,word,240FFFFF",
"patch=1,EE,0018F0D4,word,308881FC",
"patch=1,EE,0018F0D8,word,00884826",
"patch=1,EE,0018F0DC,word,3C0E0019",
"patch=1,EE,0018F0E0,word,25CEF134",
"patch=1,EE,0018F0E4,word,01C0502D",
"patch=1,EE,0018F0E8,word,240BFFFF",
"patch=1,EE,0018F0EC,word,954C0000",
"patch=1,EE,0018F0F0,word,11880005",
"patch=1,EE,0018F0F4,word,256B0001",
"patch=1,EE,0018F0F8,word,296D0011",
"patch=1,EE,0018F0FC,word,15A0FFFB",
"patch=1,EE,0018F100,word,254A0002",
"patch=1,EE,0018F104,word,0000582D",
"patch=1,EE,0018F108,word,016F5821",
"patch=1,EE,0018F10C,word,05610002",
"patch=1,EE,0018F110,word,296D0012",
"patch=1,EE,0018F114,word,256B0012",
"patch=1,EE,0018F118,word,15A00002",
"patch=1,EE,0018F11C,word,000B5840",
"patch=1,EE,0018F120,word,256BFFDC",
"patch=1,EE,0018F124,word,01CB7021",
"patch=1,EE,0018F128,word,95CC0000",
"patch=1,EE,0018F12C,word,03E00008",
"patch=1,EE,0018F130,word,012C1025",
"patch=1,EE,0018F134,word,00040000",
"patch=1,EE,0018F138,word,00080084",
"patch=1,EE,0018F13C,word,00100088",
"patch=1,EE,0018F140,word,00200090",
"patch=1,EE,0018F144,word,004000A0",
"patch=1,EE,0018F148,word,800400C0",
"patch=1,EE,0018F14C,word,80088084",
"patch=1,EE,0018F150,word,80108088",
"patch=1,EE,0018F154,word,80208090",
"patch=1,EE,0018F1E0,word,08063C35",
"patch=1,EE,0018F1E4,word,240F0001",
"patch=1,EE,0014860C,word,0C063C8E",
"patch=1,EE,00148610,word,00000000",
"patch=1,EE,00148614,word,14400014",
"patch=1,EE,00148618,word,0040182D",
"patch=1,EE,0014861C,word,1000000A",
"patch=1,EE,00148620,word,00000000",
"patch=1,EE,0018F238,word,3083007C",
"patch=1,EE,0018F23C,word,10600019",
"patch=1,EE,0018F240,word,0000102D",
"patch=1,EE,0018F244,word,70604004",
"patch=1,EE,0018F248,word,2409001E",
"patch=1,EE,0018F24C,word,01284023",
"patch=1,EE,0018F250,word,00084040",
"patch=1,EE,0018F254,word,000449C2",
"patch=1,EE,0018F258,word,31290001",
"patch=1,EE,0018F25C,word,01094021",
"patch=1,EE,0018F260,word,00044BC2",
"patch=1,EE,0018F264,word,31290001",
"patch=1,EE,0018F268,word,000950C0",
"patch=1,EE,0018F26C,word,00094840",
"patch=1,EE,0018F270,word,012A4821",
"patch=1,EE,0018F274,word,01094021",
"patch=1,EE,0018F278,word,29090008",
"patch=1,EE,0018F27C,word,15200006",
"patch=1,EE,0018F280,word,00084880",
"patch=1,EE,0018F284,word,29090010",
"patch=1,EE,0018F288,word,15200002",
"patch=1,EE,0018F28C,word,00084840",
"patch=1,EE,0018F290,word,25090010",
"patch=1,EE,0018F294,word,25290010",
"patch=1,EE,0018F298,word,25293FF0",
"patch=1,EE,0018F29C,word,03E00008",
"patch=1,EE,0018F2A0,word,0009143C",
"patch=1,EE,0018F2A4,word,03E00008",
"patch=1,EE,0018F2A8,word,00000000",
"patch=1,EE,00183668,word,0000202D",
"patch=1,EE,0018366C,word,24050020",
"patch=1,EE,00183680,word,24042000",
"patch=1,EE,00183684,word,24050008",
"patch=1,EE,00183698,word,0000202D",
"patch=1,EE,0018369C,word,24050040",
"patch=1,EE,001836B0,word,24044000",
"patch=1,EE,001836B4,word,24050004",
"patch=1,EE,001836C8,word,24050080",
"patch=1,EE,001836CC,word,0000202D",
"patch=1,EE,001836D4,word,24060002",
"patch=1,EE,001836E0,word,24041000",
"patch=1,EE,001836E4,word,24050002",
"patch=1,EE,001836F8,word,0000202D",
"patch=1,EE,001836FC,word,24050100",
"patch=1,EE,00183710,word,34048000",
"patch=1,EE,00183714,word,24050001"
]
},
{
"name": "Judge Timing Adjust",
"id": "jtime",
"lines": [
"author=Claude",
"description=判定タイミング調整。最後の行の下4桁(XXXX)が調整値で、1単位=4ms(16ビット符号付き)。0000=調整なし／FFFF=-4ms／FFFE=-8ms／FFFD=-12ms／FFFC=-16ms／FFFA=-24ms／FFF8=-32ms／0001=+4ms／0002=+8ms／0004=+16ms／0008=+32ms。マイナス=判定ラインが遅くなる(遅めに押してもジャスト)、プラス=判定ラインが早くなる。0x14D164の daddu a1,s1,zero を addiu a1,s1,調整値 に置換(判定処理に渡す時刻だけをずらすので譜面表示と音はそのまま)。上4桁(2625)は変更しないこと。",
"patch=1,EE,0014D164,word,2625FFF8"
]
},
{
"name": "COOL Judge in All Modes",
"id": "coolall",
"lines": [
"author=Claude",
"description=全モードでCOOL判定を有効化(GREAT範囲の中心±4でCOOL)し、スコア計算をCOOLありモードと同じ式にする。COOLのゲージ増加量はGREATと同じ(ゲージの仕様と表示は各モードのまま)。オートプレイ/デモもCOOLになる。画面下のカウンター欄とリザルト画面を全モードでCOOL付きにする。",
"// 0x14CBC4: COOL判定のモード条件を常に成立",
"// 0x14CFA0: オートプレイのCOOL条件を常に成立",
"// 0x14C5E8: スコア加算を全モードでCOOLありモードの式に(COOL=1000000/GREAT=500000/GOOD=100000)",
"// 0x14D640: スコア満点を全モードでCOOLありモードの式に(ノーツ数x10)",
"// 0x14B758: COOL時のゲージ増減にGREATの値を使う",
"// 0x155020: 画面下のカウンター欄の画像をCOOL付きのものに",
"// 0x216130/34/38: リザルト画面の項目パネルをモード0/1/2でもCOOL付き(EXPERTと同じ)に(モード別ジャンプテーブルの差し替え)",
"// 0x18CF6C/0x18CF7C: モード5のリザルト項目パネルをCOOL付きに(バナーあり=33/なし=43)",
"// 0x18CE50/0x18CEE0: トレーニングのリザルト項目パネルを常にCOOL付きに(バトル(3)・モード7は対象外)",
"patch=1,EE,0014CBC4,word,00000000",
"patch=1,EE,0014CFA0,word,10000039",
"patch=1,EE,0014C5E8,word,00000000",
"patch=1,EE,0014D640,word,00000000",
"patch=1,EE,0014B758,word,24040000",
"patch=1,EE,00155020,word,00000000",
"patch=1,EE,00216130,word,0018CD8C",
"patch=1,EE,00216134,word,0018CD8C",
"patch=1,EE,00216138,word,0018CD8C",
"patch=1,EE,0018CF6C,word,5040FFE1",
"patch=1,EE,0018CF7C,word,24020021",
"patch=1,EE,0018CE50,word,00000000",
"patch=1,EE,0018CEE0,word,00000000"
]
},
{
"name": "Score Formula (current pop'n)",
"id": "score",
"lines": [
"author=Claude",
"description=COOLありモードのスコア式を現行ポップンの式に変更: スコア=100000×(COOL×1.0+GREAT×0.7+GOOD×0.4)÷ポップ君総数(小数点以下切り捨て)。全モードに適用するには[COOL Judge in All Modes]も有効にする。",
"// 0x14C7A4-0x14C7A8: GREATの加算値 500000 → 700000",
"// 0x14C624-0x14C628: GOODの加算値 100000 → 400000",
"patch=1,EE,0014C624,word,3C020006",
"patch=1,EE,0014C628,word,34421A80",
"patch=1,EE,0014C7A4,word,3C02000A",
"patch=1,EE,0014C7A8,word,3442AE60"
]
},
{
"name": "No FEVER at Gauge MAX",
"id": "nofever",
"lines": [
"author=Claude",
"description=ゲージMAX時(および一部モードのコンボ99以上)にGREATがFEVER表示になるのを無効化し、常に通常のGREATとして表示する(スコアは元からGREATと同じ扱いなので変化なし)。",
"// 0x14B7B4: FEVER判定の分岐を常に通常GREAT側へ",
"patch=1,EE,0014B7B4,word,10000009"
]
},
{
"name": "PERFECT = GOOD 0 and BAD 0",
"id": "perfect",
"lines": [
"author=Claude",
"description=PERFECT(パーフェクト)の条件を「GOODとBADが0」に変更する(GREAT/COOLのみならPERFECT扱い)。COOL判定やスコア計算式の変更で満点にならない場合でもPERFECTになる。",
"// 0x1BAC60: PERFECT判定(効果音)のスコア=100000条件を「スコア>0」に変更(GOOD=0かつBAD=0は元の条件のまま)",
"// 0x18D2C8/0x18D2D4: 記録用PERFECTフラグの条件をスコア=100000からGOOD=0に変更(BAD=0はフルコンボ条件で判定済み)",
"// 0x18DD50-0x18DD5C: リザルトのPERFECT表示条件をスコア=100000からGOOD=0かつBAD=0に変更",
"patch=1,EE,0018D2C8,word,8E430014",
"patch=1,EE,0018D2D4,word,1460FFE1",
"patch=1,EE,0018DD50,word,8C830014",
"patch=1,EE,0018DD54,word,8C820018",
"patch=1,EE,0018DD58,word,00621825",
"patch=1,EE,0018DD5C,word,1060002F",
"patch=1,EE,001BAC60,word,1060000B"
]
},
{
"name": "Key Beam Length",
"id": "keybeam",
"lines": [
"author=Claude",
"description=キービームの長さを変更する。下端(判定ライン側)は固定のまま上に向かって縮み、グラデーションも縮小される。「長さ」と書いた1行の値(末尾8桁)を下の表の値に書き換えること。初期値は50%。",
"// 長さの値(元の長さ=100%、画面上のビームの高さは元約308px)",
"//    0% = 00000000 (約  0px)",
"//   10% = 0000000A (約 31px)",
"//   20% = 00000014 (約 62px)",
"//   30% = 0000001E (約 92px)",
"//   40% = 00000028 (約123px)",
"//   50% = 00000032 (約154px)",
"//   60% = 0000003C (約185px)",
"//   70% = 00000046 (約216px)",
"//   80% = 00000050 (約246px)",
"//   90% = 0000005A (約277px)",
"//  100% = 00000064 (約308px)",
"// 仕組み: ビームはテクスチャ30x308/24x308のスプライト。スプライト描画関数(0x130F60)の上端Y計算の直後(0x1310C0)に",
"//   コードを差し込み、描画する矩形が 幅30or24・高さ308 のとき、高さの拡大率(t2)を「長さ」%倍し、下端が動かないよう上端Yを下げる。",
"//   差し込みコードは空きRAM 0x000FFE00 以降、長さの値は 0x000FFF04 に置く。",
"// 長さ(この1行だけ書き換える)",
"patch=1,EE,000FFF04,word,00000032",
"// ここから下は変更しない",
"patch=1,EE,001310C0,word,0803FF80",
"patch=1,EE,000FFE00,word,1940001D",
"patch=1,EE,000FFE04,word,00000000",
"patch=1,EE,000FFE08,word,24050134",
"patch=1,EE,000FFE0C,word,1465001A",
"patch=1,EE,000FFE10,word,00000000",
"patch=1,EE,000FFE14,word,2405001E",
"patch=1,EE,000FFE18,word,11850004",
"patch=1,EE,000FFE1C,word,00000000",
"patch=1,EE,000FFE20,word,24050018",
"patch=1,EE,000FFE24,word,15850014",
"patch=1,EE,000FFE28,word,00000000",
"patch=1,EE,000FFE2C,word,3C0B0010",
"patch=1,EE,000FFE30,word,8D6BFF04",
"patch=1,EE,000FFE34,word,014B0018",
"patch=1,EE,000FFE38,word,00005812",
"patch=1,EE,000FFE3C,word,24050064",
"patch=1,EE,000FFE40,word,0165001A",
"patch=1,EE,000FFE44,word,00005812",
"patch=1,EE,000FFE48,word,014B2823",
"patch=1,EE,000FFE4C,word,00650018",
"patch=1,EE,000FFE50,word,00002812",
"patch=1,EE,000FFE54,word,01605021",
"patch=1,EE,000FFE58,word,240B0064",
"patch=1,EE,000FFE5C,word,00AB001A",
"patch=1,EE,000FFE60,word,00002812",
"patch=1,EE,000FFE64,word,44850000",
"patch=1,EE,000FFE68,word,00000000",
"patch=1,EE,000FFE6C,word,46800020",
"patch=1,EE,000FFE70,word,00000000",
"patch=1,EE,000FFE74,word,46004A40",
"patch=1,EE,000FFE78,word,3C0551EB",
"patch=1,EE,000FFE7C,word,0804C432",
"patch=1,EE,000FFE80,word,001331C0"
]
},
{
"name": "Lane Brightness",
"id": "lane",
"lines": [
"comment=Darken the key lane background. Rewrite ONLY the value at 000FFA00 (hex, 00-64):",
"comment=  100%=00000064 (original)  90%=0000005A  80%=00000050  70%=00000046  60%=0000003C",
"comment=   50%=00000032  40%=00000028  30%=0000001E  20%=00000014  10%=0000000A  0%=00000000 (black)",
"comment=Default is 70%. Only the lane background is affected (not notes/beam).",
"patch=1,EE,000FFA00,word,00000046",
"patch=1,EE,001316C8,word,0803FEC0",
"patch=1,EE,000FFB00,word,ADA000CC",
"patch=1,EE,000FFB04,word,8DA80090",
"patch=1,EE,000FFB08,word,8DA90094",
"patch=1,EE,000FFB0C,word,8DAA00C0",
"patch=1,EE,000FFB10,word,8DAB00C4",
"patch=1,EE,000FFB14,word,340C77F0",
"patch=1,EE,000FFB18,word,010C602B",
"patch=1,EE,000FFB1C,word,1580003F",
"patch=1,EE,000FFB20,word,00000000",
"patch=1,EE,000FFB24,word,340C71D0",
"patch=1,EE,000FFB28,word,012C602B",
"patch=1,EE,000FFB2C,word,1580003B",
"patch=1,EE,000FFB30,word,00000000",
"patch=1,EE,000FFB34,word,340C8801",
"patch=1,EE,000FFB38,word,014C602B",
"patch=1,EE,000FFB3C,word,11800037",
"patch=1,EE,000FFB40,word,00000000",
"patch=1,EE,000FFB44,word,340C8A01",
"patch=1,EE,000FFB48,word,016C602B",
"patch=1,EE,000FFB4C,word,11800033",
"patch=1,EE,000FFB50,word,00000000",
"patch=1,EE,000FFB54,word,01487823",
"patch=1,EE,000FFB58,word,2DEC1000",
"patch=1,EE,000FFB5C,word,1580002F",
"patch=1,EE,000FFB60,word,00000000",
"patch=1,EE,000FFB64,word,2DEC1001",
"patch=1,EE,000FFB68,word,1180002C",
"patch=1,EE,000FFB6C,word,00000000",
"patch=1,EE,000FFB70,word,0169C023",
"patch=1,EE,000FFB74,word,2F0C1600",
"patch=1,EE,000FFB78,word,15800028",
"patch=1,EE,000FFB7C,word,00000000",
"patch=1,EE,000FFB80,word,3C0C0010",
"patch=1,EE,000FFB84,word,8D8CFA00",
"patch=1,EE,000FFB88,word,240E0064",
"patch=1,EE,000FFB8C,word,8DA80080",
"patch=1,EE,000FFB90,word,010C0018",
"patch=1,EE,000FFB94,word,00004012",
"patch=1,EE,000FFB98,word,010E001A",
"patch=1,EE,000FFB9C,word,00004012",
"patch=1,EE,000FFBA0,word,ADA80080",
"patch=1,EE,000FFBA4,word,8DA80084",
"patch=1,EE,000FFBA8,word,010C0018",
"patch=1,EE,000FFBAC,word,00004012",
"patch=1,EE,000FFBB0,word,010E001A",
"patch=1,EE,000FFBB4,word,00004012",
"patch=1,EE,000FFBB8,word,ADA80084",
"patch=1,EE,000FFBBC,word,8DA80088",
"patch=1,EE,000FFBC0,word,010C0018",
"patch=1,EE,000FFBC4,word,00004012",
"patch=1,EE,000FFBC8,word,010E001A",
"patch=1,EE,000FFBCC,word,00004012",
"patch=1,EE,000FFBD0,word,ADA80088",
"patch=1,EE,000FFBD4,word,8DA800B0",
"patch=1,EE,000FFBD8,word,010C0018",
"patch=1,EE,000FFBDC,word,00004012",
"patch=1,EE,000FFBE0,word,010E001A",
"patch=1,EE,000FFBE4,word,00004012",
"patch=1,EE,000FFBE8,word,ADA800B0",
"patch=1,EE,000FFBEC,word,8DA800B4",
"patch=1,EE,000FFBF0,word,010C0018",
"patch=1,EE,000FFBF4,word,00004012",
"patch=1,EE,000FFBF8,word,010E001A",
"patch=1,EE,000FFBFC,word,00004012",
"patch=1,EE,000FFC00,word,ADA800B4",
"patch=1,EE,000FFC04,word,8DA800B8",
"patch=1,EE,000FFC08,word,010C0018",
"patch=1,EE,000FFC0C,word,00004012",
"patch=1,EE,000FFC10,word,010E001A",
"patch=1,EE,000FFC14,word,00004012",
"patch=1,EE,000FFC18,word,ADA800B8",
"patch=1,EE,000FFC1C,word,0804C5B3",
"patch=1,EE,000FFC20,word,00000000"
]
},
{
"name": "COOL Window 25ms",
"id": "coolwin",
"lines": [
"author=Claude",
"description=COOL判定の幅を±16ms(内部値±4)から現行ポップンの±25ms(内部値±6)に広げる。判定結果を決める処理の中で「時間差が-4以上かつ4以下ならCOOL」と比較している即値(-4と5)を(-6と7)に書き換えるだけで、GREAT以下の判定幅とスコア式は変えない。",
"// 内部の時間単位は1/240秒(約4.17ms)。COOL ±4=±16.7ms → ±6=±25.0ms。",
"// このタイトルのGREAT幅は内部値±12(約±50.0ms)なので、COOL ±6はGREATの内側に収まる。",
"// 幅を変えたい場合: 「-4」の行の末尾4桁を(-N)の16ビット値、「5」の行の末尾4桁を(N+1)に書き換える。",
"//   N=4(元)  FFFC / 0005    N=5  FFFB / 0006    N=6(25ms)  FFFA / 0007    N=7  FFF9 / 0008",
"// 「-4」の行は slti(時間差 < -N)、「5」の行は slti(時間差 < N+1)。「-4」の行が2つあるタイトルは、分岐の遅延スロットに入った同じ比較の複製(両方書き換える)。",
"patch=1,EE,0014CBCC,word,2A02FFFA",
"patch=1,EE,0014CC14,word,2A02FFFA",
"patch=1,EE,0014CBD8,word,2A010007"
]
},
{
"name": "480p Test (experimental)",
"id": "p480",
"lines": [
"author=Claude",
"comment=実験用。起動時にゲームを最初から起動すること（ステートのロードでは反映されない）。sceGsResetGraph を 480i→480p(inter=0, omode=0x50, ffmd=1) に変更 し、毎フレームの DISPLAY 定数を 480p 用(DX=440 DY=35 MAGH=2倍 DW=1023 DH=447)にする。512幅のまま出力するため、PCSX2 側でアスペクト比を 4:3 にして使う。",
"patch=1,EE,0013B7B0,word,24050000",
"patch=1,EE,0013B7B4,word,24060050",
"patch=1,EE,0013B7BC,word,24070001",
"patch=1,EE,0013C274,word,3463F3FF",
"patch=1,EE,0013C284,word,3C030082",
"patch=1,EE,0013C28C,word,346431B8",
"patch=1,EE,0013C290,word,346331B8"
]
}
]
},
"SLPM-66314_35E0596E": {
"gametitle": "gametitle=pop'n music 12 (CRC 35E0596E)",
"sections": [
{
"name": "HiSpeed x2-x10 with .5 steps",
"id": "hispeed",
"lines": [
"author=Claude",
"comment=OFF→2→2.5→…→9.5→10→OFF。.5は元の段階の表示、x7〜x10は x2/x2/x3/x3/x4/x4/x5 の表示（左右両方向対応）",
"patch=1,EE,0013D940,word,0804F675",
"patch=1,EE,0013D944,word,240FFFFF",
"patch=1,EE,0013D948,word,3083007C",
"patch=1,EE,0013D94C,word,10600015",
"patch=1,EE,0013D950,word,0000482D",
"patch=1,EE,0013D954,word,70604004",
"patch=1,EE,0013D958,word,2409001E",
"patch=1,EE,0013D95C,word,01284023",
"patch=1,EE,0013D960,word,00084040",
"patch=1,EE,0013D964,word,000449C2",
"patch=1,EE,0013D968,word,31290001",
"patch=1,EE,0013D96C,word,01094021",
"patch=1,EE,0013D970,word,00044BC2",
"patch=1,EE,0013D974,word,00094823",
"patch=1,EE,0013D978,word,3129000A",
"patch=1,EE,0013D97C,word,01094021",
"patch=1,EE,0013D980,word,29090008",
"patch=1,EE,0013D984,word,15200006",
"patch=1,EE,0013D988,word,00084880",
"patch=1,EE,0013D98C,word,29090010",
"patch=1,EE,0013D990,word,15200002",
"patch=1,EE,0013D994,word,00084840",
"patch=1,EE,0013D998,word,25090010",
"patch=1,EE,0013D99C,word,25290010",
"patch=1,EE,0013D9A0,word,25293FF0",
"patch=1,EE,0013D9A4,word,03E00008",
"patch=1,EE,0013D9A8,word,0009143C",
"patch=1,EE,0013D9D0,word,240F0001",
"patch=1,EE,0013D9D4,word,308880FC",
"patch=1,EE,0013D9D8,word,00884826",
"patch=1,EE,0013D9DC,word,3C0E0014",
"patch=1,EE,0013D9E0,word,25CEDA34",
"patch=1,EE,0013D9E4,word,01C0502D",
"patch=1,EE,0013D9E8,word,240BFFFF",
"patch=1,EE,0013D9EC,word,954C0000",
"patch=1,EE,0013D9F0,word,11880005",
"patch=1,EE,0013D9F4,word,256B0001",
"patch=1,EE,0013D9F8,word,296D0011",
"patch=1,EE,0013D9FC,word,15A0FFFB",
"patch=1,EE,0013DA00,word,254A0002",
"patch=1,EE,0013DA04,word,0000582D",
"patch=1,EE,0013DA08,word,016F5821",
"patch=1,EE,0013DA0C,word,05610002",
"patch=1,EE,0013DA10,word,296D0012",
"patch=1,EE,0013DA14,word,256B0012",
"patch=1,EE,0013DA18,word,15A00002",
"patch=1,EE,0013DA1C,word,000B5840",
"patch=1,EE,0013DA20,word,256BFFDC",
"patch=1,EE,0013DA24,word,01CB7021",
"patch=1,EE,0013DA28,word,95CC0000",
"patch=1,EE,0013DA2C,word,03E00008",
"patch=1,EE,0013DA30,word,012C1025",
"patch=1,EE,0013DA34,word,00040000",
"patch=1,EE,0013DA38,word,00080084",
"patch=1,EE,0013DA3C,word,00100088",
"patch=1,EE,0013DA40,word,00200090",
"patch=1,EE,0013DA44,word,004000A0",
"patch=1,EE,0013DA48,word,800400C0",
"patch=1,EE,0013DA4C,word,80088084",
"patch=1,EE,0013DA50,word,80108088",
"patch=1,EE,0013DA54,word,80208090",
"patch=1,EE,001467F4,word,0C04F652",
"patch=1,EE,001467F8,word,00000000",
"patch=1,EE,001467FC,word,14400014",
"patch=1,EE,00146800,word,0040182D",
"patch=1,EE,00146804,word,1000000A",
"patch=1,EE,00146808,word,00000000"
]
},
{
"name": "Judge Timing Adjust",
"id": "jtime",
"lines": [
"author=Claude",
"description=判定タイミング調整。最後の行の下4桁(XXXX)が調整値で、1単位=4ms(16ビット符号付き)。0000=調整なし／FFFF=-4ms／FFFE=-8ms／FFFD=-12ms／FFFC=-16ms／FFFA=-24ms／FFF8=-32ms／0001=+4ms／0002=+8ms／0004=+16ms／0008=+32ms。マイナス=判定ラインが遅くなる(遅めに押してもジャスト)、プラス=判定ラインが早くなる。0x14B50Cの daddu a1,s0,zero を addiu a1,s0,調整値 に置換(判定処理に渡す時刻だけをずらすので譜面表示と音はそのまま)。上4桁(2605)は変更しないこと。",
"patch=1,EE,0014B50C,word,2605FFF8"
]
},
{
"name": "COOL Judge in All Modes",
"id": "coolall",
"lines": [
"author=Claude",
"description=全モードでCOOL判定を有効化(GREAT範囲の中心±4でCOOL)し、スコア計算をCOOLありモードと同じ式にする。COOLのゲージ増加量はGREATと同じ(ゲージの仕様と表示は各モードのまま)。オートプレイ/デモもCOOLになる。画面下のカウンター欄とリザルト画面を全モードでCOOL付きにする。",
"// 0x14AE54: COOL判定のモード条件を常に成立",
"// 0x14B2C8: オートプレイのCOOL条件を常に成立",
"// 0x14A858: スコア加算を全モードでCOOLありモードの式に(COOL=1000000/GREAT=500000/GOOD=100000)",
"// 0x14BA80: スコア満点を全モードでCOOLありモードの式に(ノーツ数x10)",
"// 0x149788: COOL時のゲージ増減にGREATの値を使う",
"// 0x153CEC/0x15412C: 画面下のカウンター欄をCOOL付きの並びにしてCOOLの数を表示",
"// 0x1669E4/0x166B08/0x166D84/0x1676B8/0x167788/0x1678F0/0x167EC8/0x169DE0/0x16B000: リザルト画面のCOOL判定チェックを常に成立(COOL行と配置をCOOLありモードと同じに。リザルトのゲージ部分は対象外)",
"// 0x166F98: リザルト画面の曲バナー表示を省略(COOLありモードと同じく、COOL行と重ならないようにする)",
"patch=1,EE,0014AE54,word,00000000",
"patch=1,EE,0014B2C8,word,10000076",
"patch=1,EE,0014A858,word,00000000",
"patch=1,EE,0014BA80,word,00000000",
"patch=1,EE,00149788,word,00000000",
"patch=1,EE,00153CEC,word,24030001",
"patch=1,EE,0015412C,word,24030001",
"patch=1,EE,001669E4,word,24020001",
"patch=1,EE,00166B08,word,24020001",
"patch=1,EE,00166D84,word,24020001",
"patch=1,EE,001676B8,word,24020001",
"patch=1,EE,00167788,word,24020001",
"patch=1,EE,001678F0,word,24020001",
"patch=1,EE,00167EC8,word,24020001",
"patch=1,EE,00169DE0,word,24020001",
"patch=1,EE,0016B000,word,24020001",
"patch=1,EE,00166F98,word,10000014"
]
},
{
"name": "Score Formula (current pop'n)",
"id": "score",
"lines": [
"author=Claude",
"description=COOLありモードのスコア式を現行ポップンの式に変更: スコア=100000×(COOL×1.0+GREAT×0.7+GOOD×0.4)÷ポップ君総数(小数点以下切り捨て)。全モードに適用するには[COOL Judge in All Modes]も有効にする。",
"// 0x14AA20-0x14AA24: GREATの加算値 500000 → 700000",
"// 0x14A894-0x14A898: GOODの加算値 100000 → 400000",
"patch=1,EE,0014AA20,word,3C02000A",
"patch=1,EE,0014AA24,word,3442AE60",
"patch=1,EE,0014A894,word,3C020006",
"patch=1,EE,0014A898,word,34421A80"
]
},
{
"name": "No FEVER at Gauge MAX",
"id": "nofever",
"lines": [
"author=Claude",
"description=ゲージMAX時(および一部モードのコンボ99以上)にGREATがFEVER表示になるのを無効化し、常に通常のGREATとして表示する(スコアは元からGREATと同じ扱いなので変化なし)。",
"// 0x149818: FEVER判定の分岐を常に通常GREAT側へ",
"patch=1,EE,00149818,word,10000011"
]
},
{
"name": "PERFECT = GOOD 0 and BAD 0",
"id": "perfect",
"lines": [
"author=Claude",
"description=PERFECT(パーフェクト)の条件を「GOODとBADが0」に変更する(GREAT/COOLのみならPERFECT扱い)。COOL判定やスコア計算式の変更で満点にならない場合でもPERFECTになる。",
"// 0x161020: PERFECT判定(効果音)のスコア=100000条件を「スコア>0」に変更(GOOD=0かつBAD=0は元の条件のまま)",
"// 0x165FAC/0x165FB8: 記録用PERFECTフラグの条件をスコア=100000からGOOD=0に変更(BAD=0はフルコンボ条件で判定済み)",
"// 0x16AF3C-0x16AF50: リザルトのPERFECT表示条件をスコア=100000からGOOD=0かつBAD=0に変更",
"patch=1,EE,00161020,word,1060000B",
"patch=1,EE,00165FAC,word,8E430014",
"patch=1,EE,00165FB8,word,14600004",
"patch=1,EE,0016AF3C,word,3C0200CB",
"patch=1,EE,0016AF40,word,8C43B02C",
"patch=1,EE,0016AF44,word,8C44B030",
"patch=1,EE,0016AF48,word,00641825",
"patch=1,EE,0016AF4C,word,10600091",
"patch=1,EE,0016AF50,word,00000000"
]
},
{
"name": "Key Beam Length",
"id": "keybeam",
"lines": [
"author=Claude",
"description=キービームの長さを変更する。下端(判定ライン側)は固定のまま上に向かって縮み、グラデーションも縮小される。「長さ」と書いた1行の値(末尾8桁)を下の表の値に書き換えること。初期値は50%。",
"// 長さの値(元の長さ=100%、画面上のビームの高さは元約308px)",
"//    0% = 00000000 (約  0px)",
"//   10% = 0000000A (約 31px)",
"//   20% = 00000014 (約 62px)",
"//   30% = 0000001E (約 92px)",
"//   40% = 00000028 (約123px)",
"//   50% = 00000032 (約154px)",
"//   60% = 0000003C (約185px)",
"//   70% = 00000046 (約216px)",
"//   80% = 00000050 (約246px)",
"//   90% = 0000005A (約277px)",
"//  100% = 00000064 (約308px)",
"// 仕組み: ビームはテクスチャ30x308/24x308のスプライト。スプライト描画関数(0x128840)の上端Y計算の直後(0x128A74)に",
"//   コードを差し込み、描画する矩形が 幅30or24・高さ308 のとき、高さの拡大率(s2)を「長さ」%倍し、下端が動かないよう上端Yを下げる。",
"//   差し込みコードは空きRAM 0x000FFE00 以降、長さの値は 0x000FFF04 に置く。",
"// 長さ(この1行だけ書き換える)",
"patch=1,EE,000FFF04,word,00000032",
"// ここから下は変更しない",
"patch=1,EE,00128A74,word,0803FF80",
"patch=1,EE,000FFE00,word,1A40001F",
"patch=1,EE,000FFE04,word,00000000",
"patch=1,EE,000FFE08,word,868B0006",
"patch=1,EE,000FFE0C,word,240C0134",
"patch=1,EE,000FFE10,word,156C001B",
"patch=1,EE,000FFE14,word,00000000",
"patch=1,EE,000FFE18,word,868A0004",
"patch=1,EE,000FFE1C,word,240C001E",
"patch=1,EE,000FFE20,word,114C0004",
"patch=1,EE,000FFE24,word,00000000",
"patch=1,EE,000FFE28,word,240C0018",
"patch=1,EE,000FFE2C,word,154C0014",
"patch=1,EE,000FFE30,word,00000000",
"patch=1,EE,000FFE34,word,3C0A0010",
"patch=1,EE,000FFE38,word,8D4AFF04",
"patch=1,EE,000FFE3C,word,024A0018",
"patch=1,EE,000FFE40,word,00005012",
"patch=1,EE,000FFE44,word,240C0064",
"patch=1,EE,000FFE48,word,014C001A",
"patch=1,EE,000FFE4C,word,00005012",
"patch=1,EE,000FFE50,word,024A6023",
"patch=1,EE,000FFE54,word,016C0018",
"patch=1,EE,000FFE58,word,00006012",
"patch=1,EE,000FFE5C,word,01409021",
"patch=1,EE,000FFE60,word,240B0064",
"patch=1,EE,000FFE64,word,018B001A",
"patch=1,EE,000FFE68,word,00006012",
"patch=1,EE,000FFE6C,word,448C0000",
"patch=1,EE,000FFE70,word,00000000",
"patch=1,EE,000FFE74,word,46800020",
"patch=1,EE,000FFE78,word,00000000",
"patch=1,EE,000FFE7C,word,46004A40",
"patch=1,EE,000FFE80,word,8FAA00F8",
"patch=1,EE,000FFE84,word,0804A29E",
"patch=1,EE,000FFE88,word,00000000"
]
},
{
"name": "Lane Brightness",
"id": "lane",
"lines": [
"comment=Darken the key lane background. Rewrite ONLY the value at 000FFA00 (hex, 00-64):",
"comment=  100%=00000064 (original)  90%=0000005A  80%=00000050  70%=00000046  60%=0000003C",
"comment=   50%=00000032  40%=00000028  30%=0000001E  20%=00000014  10%=0000000A  0%=00000000 (black)",
"comment=Default is 70%. Only the lane background is affected (not notes/beam).",
"patch=1,EE,000FFA00,word,00000046",
"patch=1,EE,001290A4,word,0803FEC0",
"patch=1,EE,000FFB00,word,ACA000CC",
"patch=1,EE,000FFB04,word,8CA80090",
"patch=1,EE,000FFB08,word,8CA90094",
"patch=1,EE,000FFB0C,word,8CAA00C0",
"patch=1,EE,000FFB10,word,8CAB00C4",
"patch=1,EE,000FFB14,word,340C77F0",
"patch=1,EE,000FFB18,word,010C602B",
"patch=1,EE,000FFB1C,word,1580003F",
"patch=1,EE,000FFB20,word,00000000",
"patch=1,EE,000FFB24,word,340C6FF0",
"patch=1,EE,000FFB28,word,012C602B",
"patch=1,EE,000FFB2C,word,1580003B",
"patch=1,EE,000FFB30,word,00000000",
"patch=1,EE,000FFB34,word,340C8801",
"patch=1,EE,000FFB38,word,014C602B",
"patch=1,EE,000FFB3C,word,11800037",
"patch=1,EE,000FFB40,word,00000000",
"patch=1,EE,000FFB44,word,340C8A01",
"patch=1,EE,000FFB48,word,016C602B",
"patch=1,EE,000FFB4C,word,11800033",
"patch=1,EE,000FFB50,word,00000000",
"patch=1,EE,000FFB54,word,01487823",
"patch=1,EE,000FFB58,word,2DEC0F60",
"patch=1,EE,000FFB5C,word,1580002F",
"patch=1,EE,000FFB60,word,00000000",
"patch=1,EE,000FFB64,word,2DEC0F61",
"patch=1,EE,000FFB68,word,1180002C",
"patch=1,EE,000FFB6C,word,00000000",
"patch=1,EE,000FFB70,word,0169C023",
"patch=1,EE,000FFB74,word,2F0C1600",
"patch=1,EE,000FFB78,word,15800028",
"patch=1,EE,000FFB7C,word,00000000",
"patch=1,EE,000FFB80,word,3C0C0010",
"patch=1,EE,000FFB84,word,8D8CFA00",
"patch=1,EE,000FFB88,word,240D0064",
"patch=1,EE,000FFB8C,word,8CA80080",
"patch=1,EE,000FFB90,word,010C0018",
"patch=1,EE,000FFB94,word,00004012",
"patch=1,EE,000FFB98,word,010D001A",
"patch=1,EE,000FFB9C,word,00004012",
"patch=1,EE,000FFBA0,word,ACA80080",
"patch=1,EE,000FFBA4,word,8CA80084",
"patch=1,EE,000FFBA8,word,010C0018",
"patch=1,EE,000FFBAC,word,00004012",
"patch=1,EE,000FFBB0,word,010D001A",
"patch=1,EE,000FFBB4,word,00004012",
"patch=1,EE,000FFBB8,word,ACA80084",
"patch=1,EE,000FFBBC,word,8CA80088",
"patch=1,EE,000FFBC0,word,010C0018",
"patch=1,EE,000FFBC4,word,00004012",
"patch=1,EE,000FFBC8,word,010D001A",
"patch=1,EE,000FFBCC,word,00004012",
"patch=1,EE,000FFBD0,word,ACA80088",
"patch=1,EE,000FFBD4,word,8CA800B0",
"patch=1,EE,000FFBD8,word,010C0018",
"patch=1,EE,000FFBDC,word,00004012",
"patch=1,EE,000FFBE0,word,010D001A",
"patch=1,EE,000FFBE4,word,00004012",
"patch=1,EE,000FFBE8,word,ACA800B0",
"patch=1,EE,000FFBEC,word,8CA800B4",
"patch=1,EE,000FFBF0,word,010C0018",
"patch=1,EE,000FFBF4,word,00004012",
"patch=1,EE,000FFBF8,word,010D001A",
"patch=1,EE,000FFBFC,word,00004012",
"patch=1,EE,000FFC00,word,ACA800B4",
"patch=1,EE,000FFC04,word,8CA800B8",
"patch=1,EE,000FFC08,word,010C0018",
"patch=1,EE,000FFC0C,word,00004012",
"patch=1,EE,000FFC10,word,010D001A",
"patch=1,EE,000FFC14,word,00004012",
"patch=1,EE,000FFC18,word,ACA800B8",
"patch=1,EE,000FFC1C,word,0804A42A",
"patch=1,EE,000FFC20,word,00000000"
]
},
{
"name": "COOL Window 25ms",
"id": "coolwin",
"lines": [
"author=Claude",
"description=COOL判定の幅を±16ms(内部値±4)から現行ポップンの±25ms(内部値±6)に広げる。判定結果を決める処理の中で「時間差が-4以上かつ4以下ならCOOL」と比較している即値(-4と5)を(-6と7)に書き換えるだけで、GREAT以下の判定幅とスコア式は変えない。",
"// 内部の時間単位は1/240秒(約4.17ms)。COOL ±4=±16.7ms → ±6=±25.0ms。",
"// このタイトルのGREAT幅は内部値±8(約±33.3ms)なので、COOL ±6はGREATの内側に収まる。",
"// 幅を変えたい場合: 「-4」の行の末尾4桁を(-N)の16ビット値、「5」の行の末尾4桁を(N+1)に書き換える。",
"//   N=4(元)  FFFC / 0005    N=5  FFFB / 0006    N=6(25ms)  FFFA / 0007    N=7  FFF9 / 0008",
"// 「-4」の行は slti(時間差 < -N)、「5」の行は slti(時間差 < N+1)。「-4」の行が2つあるタイトルは、分岐の遅延スロットに入った同じ比較の複製(両方書き換える)。",
"patch=1,EE,0014AE5C,word,2A22FFFA",
"patch=1,EE,0014AEB4,word,2A22FFFA",
"patch=1,EE,0014AE68,word,2A210007"
]
},
{
"name": "480p Test (experimental)",
"id": "p480",
"lines": [
"author=Claude",
"comment=実験用。起動時にゲームを最初から起動すること（ステートのロードでは反映されない）。sceGsResetGraph を 480i→480p(inter=0, omode=0x50, ffmd=1) に変更し、毎フレームの DISPLAY 定数を 480p 用(DX=440 DY=35 MAGH=2倍 DW=1023 DH=447)にする。512幅のまま出力するため、PCSX2 側でアスペクト比を 4:3 にして使う。",
"patch=1,EE,00133400,word,24050000",
"patch=1,EE,00133404,word,24060050",
"patch=1,EE,0013340C,word,24070001",
"patch=1,EE,00133E8C,word,3463F3FF",
"patch=1,EE,00133E9C,word,3C030082",
"patch=1,EE,00133EA4,word,346431B8",
"patch=1,EE,00133EA8,word,346331B8"
]
}
]
},
"SLPM-66533_4BD5C7E6": {
"gametitle": "gametitle=pop'n music 13 (CRC 4BD5C7E6)",
"sections": [
{
"name": "HiSpeed x2-x10 with .5 steps",
"id": "hispeed",
"lines": [
"author=Claude",
"comment=OFF→2→2.5→…→9.5→10→OFF（左右どちらの方向にも対応）。.5は元の段階の表示、x7〜x10は x2/x2/x3/x3/x4/x4/x5 の表示",
"patch=1,EE,00136FD0,word,0804DC19",
"patch=1,EE,00136FD4,word,240FFFFF",
"patch=1,EE,00136FD8,word,3083007C",
"patch=1,EE,00136FDC,word,10600015",
"patch=1,EE,00136FE0,word,0000482D",
"patch=1,EE,00136FE4,word,70604004",
"patch=1,EE,00136FE8,word,2409001E",
"patch=1,EE,00136FEC,word,01284023",
"patch=1,EE,00136FF0,word,00084040",
"patch=1,EE,00136FF4,word,000449C2",
"patch=1,EE,00136FF8,word,31290001",
"patch=1,EE,00136FFC,word,01094021",
"patch=1,EE,00137000,word,00044BC2",
"patch=1,EE,00137004,word,00094823",
"patch=1,EE,00137008,word,3129000A",
"patch=1,EE,0013700C,word,01094021",
"patch=1,EE,00137010,word,29090008",
"patch=1,EE,00137014,word,15200006",
"patch=1,EE,00137018,word,00084880",
"patch=1,EE,0013701C,word,29090010",
"patch=1,EE,00137020,word,15200002",
"patch=1,EE,00137024,word,00084840",
"patch=1,EE,00137028,word,25090010",
"patch=1,EE,0013702C,word,25290010",
"patch=1,EE,00137030,word,25293FF0",
"patch=1,EE,00137034,word,03E00008",
"patch=1,EE,00137038,word,0009143C",
"patch=1,EE,00137060,word,240F0001",
"patch=1,EE,00137064,word,308880FC",
"patch=1,EE,00137068,word,00884826",
"patch=1,EE,0013706C,word,3C0E0013",
"patch=1,EE,00137070,word,25CE70C4",
"patch=1,EE,00137074,word,01C0502D",
"patch=1,EE,00137078,word,240BFFFF",
"patch=1,EE,0013707C,word,954C0000",
"patch=1,EE,00137080,word,11880005",
"patch=1,EE,00137084,word,256B0001",
"patch=1,EE,00137088,word,296D0011",
"patch=1,EE,0013708C,word,15A0FFFB",
"patch=1,EE,00137090,word,254A0002",
"patch=1,EE,00137094,word,0000582D",
"patch=1,EE,00137098,word,016F5821",
"patch=1,EE,0013709C,word,05610002",
"patch=1,EE,001370A0,word,296D0012",
"patch=1,EE,001370A4,word,256B0012",
"patch=1,EE,001370A8,word,15A00002",
"patch=1,EE,001370AC,word,000B5840",
"patch=1,EE,001370B0,word,256BFFDC",
"patch=1,EE,001370B4,word,01CB7021",
"patch=1,EE,001370B8,word,95CC0000",
"patch=1,EE,001370BC,word,03E00008",
"patch=1,EE,001370C0,word,012C1025",
"patch=1,EE,001370C4,word,00040000",
"patch=1,EE,001370C8,word,00080084",
"patch=1,EE,001370CC,word,00100088",
"patch=1,EE,001370D0,word,00200090",
"patch=1,EE,001370D4,word,004000A0",
"patch=1,EE,001370D8,word,800400C0",
"patch=1,EE,001370DC,word,80088084",
"patch=1,EE,001370E0,word,80108088",
"patch=1,EE,001370E4,word,80208090",
"patch=1,EE,00161EE4,word,0C04DBF6",
"patch=1,EE,00161EE8,word,00000000",
"patch=1,EE,00161EEC,word,14400014",
"patch=1,EE,00161EF0,word,0040182D",
"patch=1,EE,00161EF4,word,1000000A",
"patch=1,EE,00161EF8,word,00000000"
]
},
{
"name": "Score Formula (current pop'n)",
"id": "score",
"lines": [
"author=Claude",
"description=COOLありのスコア式を現行ポップンの式に変更: スコア=100000×(COOL×1.0+GREAT×0.7+GOOD×0.4)÷ポップ君総数(小数点以下切り捨て)。",
"// 0x1660BC-0x1660C0: GREATの加算値 500000 → 700000",
"// 0x165F64-0x165F68: GOODの加算値 100000 → 400000",
"patch=1,EE,001660BC,word,3C02000A",
"patch=1,EE,001660C0,word,3442AE60",
"patch=1,EE,00165F64,word,3C020006",
"patch=1,EE,00165F68,word,34421A80"
]
},
{
"name": "FREE COOL Default ON",
"id": "freecool",
"lines": [
"author=Claude",
"description=FREEモードのCOOL判定オプションの初期値をONにする(初期化時にOFF(0)を書き込む処理をON(1)に変更)。オプション画面でOFFに切り替えることは従来どおり可能。",
"// 0x1B2504: sw zero → sw a0(この時点でa0=1)",
"patch=1,EE,001B2504,word,AF848C40"
]
},
{
"name": "Key Beam Length",
"id": "keybeam",
"lines": [
"author=Claude",
"description=キービームの長さを変更する。下端(判定ライン側)は固定のまま上に向かって縮み、グラデーションも縮小される。「長さ」と書いた1行の値(末尾8桁)を下の表の値に書き換えること。初期値は50%。",
"// 長さの値(元の長さ=100%、画面上のビームの高さは元約308px)",
"//    0% = 00000000 (約  0px)",
"//   10% = 0000000A (約 31px)",
"//   20% = 00000014 (約 62px)",
"//   30% = 0000001E (約 92px)",
"//   40% = 00000028 (約123px)",
"//   50% = 00000032 (約154px)",
"//   60% = 0000003C (約185px)",
"//   70% = 00000046 (約216px)",
"//   80% = 00000050 (約246px)",
"//   90% = 0000005A (約277px)",
"//  100% = 00000064 (約308px)",
"// 仕組み: ビームはテクスチャ30x308/24x308のスプライト。スプライト描画関数(0x12A850)がGSパケットを書き終える箇所(0x12B13C)に",
"//   コードを差し込み、パケットのUV矩形が 幅30or24・高さ308 のとき、上端の頂点Yを「(100-長さ)%」ぶん下げて、下端を動かさずに縮める。",
"//   差し込みコードは空きRAM 0x000FFE00 以降、長さの値は 0x000FFF04 に置く。",
"// 長さ(この1行だけ書き換える)",
"patch=1,EE,000FFF04,word,00000032",
"// ここから下は変更しない",
"patch=1,EE,0012B13C,word,0803FF80",
"patch=1,EE,000FFE00,word,8E6800A0",
"patch=1,EE,000FFE04,word,8E6900D0",
"patch=1,EE,000FFE08,word,01284823",
"patch=1,EE,000FFE0C,word,240A01E0",
"patch=1,EE,000FFE10,word,112A0004",
"patch=1,EE,000FFE14,word,00000000",
"patch=1,EE,000FFE18,word,240A0180",
"patch=1,EE,000FFE1C,word,152A0016",
"patch=1,EE,000FFE20,word,00000000",
"patch=1,EE,000FFE24,word,8E6800A4",
"patch=1,EE,000FFE28,word,8E6900D4",
"patch=1,EE,000FFE2C,word,01284823",
"patch=1,EE,000FFE30,word,240A1340",
"patch=1,EE,000FFE34,word,152A0010",
"patch=1,EE,000FFE38,word,00000000",
"patch=1,EE,000FFE3C,word,8E6800C4",
"patch=1,EE,000FFE40,word,8E6900F4",
"patch=1,EE,000FFE44,word,01284823",
"patch=1,EE,000FFE48,word,1920000B",
"patch=1,EE,000FFE4C,word,00000000",
"patch=1,EE,000FFE50,word,3C0A0010",
"patch=1,EE,000FFE54,word,8D4AFF04",
"patch=1,EE,000FFE58,word,240B0064",
"patch=1,EE,000FFE5C,word,016A5023",
"patch=1,EE,000FFE60,word,012A0018",
"patch=1,EE,000FFE64,word,00005012",
"patch=1,EE,000FFE68,word,014B001A",
"patch=1,EE,000FFE6C,word,00005012",
"patch=1,EE,000FFE70,word,010A4021",
"patch=1,EE,000FFE74,word,AE6800C4",
"patch=1,EE,000FFE78,word,24030010",
"patch=1,EE,000FFE7C,word,0804AC50",
"patch=1,EE,000FFE80,word,00000000"
]
},
{
"name": "Lane Brightness",
"id": "lane",
"lines": [
"comment=Darken the key lane background. Rewrite ONLY the value at 000FFA00 (hex, 00-64):",
"comment=  100%=00000064 (original)  90%=0000005A  80%=00000050  70%=00000046  60%=0000003C",
"comment=   50%=00000032  40%=00000028  30%=0000001E  20%=00000014  10%=0000000A  0%=00000000 (black)",
"comment=Default is 70%. Only the lane background is affected (not notes/beam).",
"patch=1,EE,000FFA00,word,00000046",
"patch=1,EE,0012B144,word,0803FEC0",
"patch=1,EE,000FFB00,word,AE6000FC",
"patch=1,EE,000FFB04,word,8E6800C0",
"patch=1,EE,000FFB08,word,8E6900C4",
"patch=1,EE,000FFB0C,word,8E6A00F0",
"patch=1,EE,000FFB10,word,8E6B00F4",
"patch=1,EE,000FFB14,word,340C77F0",
"patch=1,EE,000FFB18,word,010C602B",
"patch=1,EE,000FFB1C,word,15800042",
"patch=1,EE,000FFB20,word,00000000",
"patch=1,EE,000FFB24,word,340C6FF0",
"patch=1,EE,000FFB28,word,012C602B",
"patch=1,EE,000FFB2C,word,1580003E",
"patch=1,EE,000FFB30,word,00000000",
"patch=1,EE,000FFB34,word,340C8801",
"patch=1,EE,000FFB38,word,014C602B",
"patch=1,EE,000FFB3C,word,1180003A",
"patch=1,EE,000FFB40,word,00000000",
"patch=1,EE,000FFB44,word,340C8A01",
"patch=1,EE,000FFB48,word,016C602B",
"patch=1,EE,000FFB4C,word,11800036",
"patch=1,EE,000FFB50,word,00000000",
"patch=1,EE,000FFB54,word,01487823",
"patch=1,EE,000FFB58,word,2DEC0F40",
"patch=1,EE,000FFB5C,word,15800032",
"patch=1,EE,000FFB60,word,00000000",
"patch=1,EE,000FFB64,word,2DEC0F41",
"patch=1,EE,000FFB68,word,1180002F",
"patch=1,EE,000FFB6C,word,00000000",
"patch=1,EE,000FFB70,word,0169C023",
"patch=1,EE,000FFB74,word,2F0C1400",
"patch=1,EE,000FFB78,word,1580002B",
"patch=1,EE,000FFB7C,word,00000000",
"patch=1,EE,000FFB80,word,2F0C1401",
"patch=1,EE,000FFB84,word,11800028",
"patch=1,EE,000FFB88,word,00000000",
"patch=1,EE,000FFB8C,word,3C0C0010",
"patch=1,EE,000FFB90,word,8D8CFA00",
"patch=1,EE,000FFB94,word,240D0064",
"patch=1,EE,000FFB98,word,8E6800B0",
"patch=1,EE,000FFB9C,word,010C0018",
"patch=1,EE,000FFBA0,word,00004012",
"patch=1,EE,000FFBA4,word,010D001A",
"patch=1,EE,000FFBA8,word,00004012",
"patch=1,EE,000FFBAC,word,AE6800B0",
"patch=1,EE,000FFBB0,word,8E6800B4",
"patch=1,EE,000FFBB4,word,010C0018",
"patch=1,EE,000FFBB8,word,00004012",
"patch=1,EE,000FFBBC,word,010D001A",
"patch=1,EE,000FFBC0,word,00004012",
"patch=1,EE,000FFBC4,word,AE6800B4",
"patch=1,EE,000FFBC8,word,8E6800B8",
"patch=1,EE,000FFBCC,word,010C0018",
"patch=1,EE,000FFBD0,word,00004012",
"patch=1,EE,000FFBD4,word,010D001A",
"patch=1,EE,000FFBD8,word,00004012",
"patch=1,EE,000FFBDC,word,AE6800B8",
"patch=1,EE,000FFBE0,word,8E6800E0",
"patch=1,EE,000FFBE4,word,010C0018",
"patch=1,EE,000FFBE8,word,00004012",
"patch=1,EE,000FFBEC,word,010D001A",
"patch=1,EE,000FFBF0,word,00004012",
"patch=1,EE,000FFBF4,word,AE6800E0",
"patch=1,EE,000FFBF8,word,8E6800E4",
"patch=1,EE,000FFBFC,word,010C0018",
"patch=1,EE,000FFC00,word,00004012",
"patch=1,EE,000FFC04,word,010D001A",
"patch=1,EE,000FFC08,word,00004012",
"patch=1,EE,000FFC0C,word,AE6800E4",
"patch=1,EE,000FFC10,word,8E6800E8",
"patch=1,EE,000FFC14,word,010C0018",
"patch=1,EE,000FFC18,word,00004012",
"patch=1,EE,000FFC1C,word,010D001A",
"patch=1,EE,000FFC20,word,00004012",
"patch=1,EE,000FFC24,word,AE6800E8",
"patch=1,EE,000FFC28,word,0804AC52",
"patch=1,EE,000FFC2C,word,00000000"
]
},
{
"name": "Judge Adjust 4ms Step",
"id": "jstep",
"lines": [
"author=Claude",
"description=判定調整を4ms刻みにする。元は1段階=約16ms(1単位=4msの4倍)。このパッチでは内部の設定値の1段階=4ms(元の1/4)にし、設定画面の操作範囲を内部値-60〜+60(=表示-15〜+15のまま、±240ms)に広げる。表示は「内部値÷4(0方向に切り捨て)」なので、見た目は今まで通り整数のみ(内部が-2なら表示0、-6なら表示-1)。左右ボタン1回で4ms動き、表示は4回ごとに変わる。",
"// 仕組み(popn13): 設定値は符号付き1バイト(保存先0x00CED5C0、設定画面中は0x0025031C)。",
"//   0x161370/0x161384/0x168374: ゲーム内で設定値に掛ける倍率を ×4 → ×1 に(1単位=4ms)",
"//   0x1F3530/0x1F353C/0x1F37A0/0x1F37AC: 設定画面の範囲(元は-15〜+15で端を越えると反対側へ)を-60〜+60に",
"//   0x1F2BFC → 0x000FFD00: 設定画面の表示用に設定値を読む命令を、÷4(0方向切り捨て)して返す短いコードに差し替え",
"// 注意: この4msパッチを入れる前に保存した設定値(-15〜+15)は、内部値として読まれるため効果が1/4に見える。設定画面で入れ直すこと。",
"patch=1,EE,00161370,word,00021000",
"patch=1,EE,00161384,word,00021000",
"patch=1,EE,00168374,word,00021800",
"patch=1,EE,001F3530,word,2841FFC4",
"patch=1,EE,001F353C,word,2402003C",
"patch=1,EE,001F37A0,word,2841003D",
"patch=1,EE,001F37AC,word,2402FFC4",
"patch=1,EE,001F2BFC,word,0803FF40",
"patch=1,EE,000FFD00,word,8386902C",
"patch=1,EE,000FFD04,word,00060FC3",
"patch=1,EE,000FFD08,word,00010F82",
"patch=1,EE,000FFD0C,word,00C13021",
"patch=1,EE,000FFD10,word,0807CB01",
"patch=1,EE,000FFD14,word,00063083"
]
},
{
"name": "COOL Window 25ms",
"id": "coolwin",
"lines": [
"author=Claude",
"description=COOL判定の幅を±16ms(内部値±4)から現行ポップンの±25ms(内部値±6)に広げる。判定結果を決める処理の中で「時間差が-4以上かつ4以下ならCOOL」と比較している即値(-4と5)を(-6と7)に書き換えるだけで、GREAT以下の判定幅とスコア式は変えない。",
"// 内部の時間単位は1/240秒(約4.17ms)。COOL ±4=±16.7ms → ±6=±25.0ms。",
"// このタイトルのGREAT幅は内部値±12(約±50.0ms)なので、COOL ±6はGREATの内側に収まる。",
"// 幅を変えたい場合: 「-4」の行の末尾4桁を(-N)の16ビット値、「5」の行の末尾4桁を(N+1)に書き換える。",
"//   N=4(元)  FFFC / 0005    N=5  FFFB / 0006    N=6(25ms)  FFFA / 0007    N=7  FFF9 / 0008",
"// 「-4」の行は slti(時間差 < -N)、「5」の行は slti(時間差 < N+1)。「-4」の行が2つあるタイトルは、分岐の遅延スロットに入った同じ比較の複製(両方書き換える)。",
"patch=1,EE,00166568,word,2A02FFFA",
"patch=1,EE,00166574,word,2A010007"
]
},
{
"name": "480p Test (experimental)",
"id": "p480",
"lines": [
"author=Claude",
"comment=実験用。起動時にゲームを最初から起動すること（ステートのロードでは反映されない）。sceGsResetGraph を 480i→480p(inter=0, omode=0x50, ffmd=1) に変更し、毎フレームの DISPLAY 定数を 480p 用(DX=440 DY=35 MAGH=2倍 DW=1023 DH=447)にする。512幅のまま出力するため、PCSX2 側でアスペクト比を 4:3 にして使う。",
"patch=1,EE,001352F0,word,24050000",
"patch=1,EE,001352F4,word,24060050",
"patch=1,EE,001352FC,word,24070001",
"patch=1,EE,00135E14,word,3463F3FF",
"patch=1,EE,00135E24,word,3C030082",
"patch=1,EE,00135E2C,word,346431B8",
"patch=1,EE,00135E30,word,346331B8"
]
}
]
},
"SLPM-66742_632DB211": {
"gametitle": "gametitle=pop'n music 14 FEVER! (CRC 632DB211)",
"sections": [
{
"name": "HiSpeed extended to x8 (max-safe)",
"id": "hispeed",
"lines": [
"author=Claude",
"comment=OFF→1.5→…→6.0→6.5→7.0→7.5→8(上限ぎりぎり)→OFF（両方向）",
"patch=1,EE,00143550,word,240FFFFF",
"patch=1,EE,00143554,word,30880FFC",
"patch=1,EE,00143558,word,00884826",
"patch=1,EE,0014355C,word,3C0E0014",
"patch=1,EE,00143560,word,25CE35B4",
"patch=1,EE,00143564,word,01C0502D",
"patch=1,EE,00143568,word,240BFFFF",
"patch=1,EE,0014356C,word,954C0000",
"patch=1,EE,00143570,word,11880005",
"patch=1,EE,00143574,word,256B0001",
"patch=1,EE,00143578,word,296D000E",
"patch=1,EE,0014357C,word,15A0FFFB",
"patch=1,EE,00143580,word,254A0002",
"patch=1,EE,00143584,word,0000582D",
"patch=1,EE,00143588,word,016F5821",
"patch=1,EE,0014358C,word,05610002",
"patch=1,EE,00143590,word,296D000F",
"patch=1,EE,00143594,word,256B000F",
"patch=1,EE,00143598,word,15A00002",
"patch=1,EE,0014359C,word,000B5840",
"patch=1,EE,001435A0,word,256BFFE2",
"patch=1,EE,001435A4,word,01CB7021",
"patch=1,EE,001435A8,word,95CC0000",
"patch=1,EE,001435AC,word,03E00008",
"patch=1,EE,001435B0,word,012C1025",
"patch=1,EE,001435B4,word,00040000",
"patch=1,EE,001435B8,word,00100008",
"patch=1,EE,001435BC,word,00400020",
"patch=1,EE,001435C0,word,01000080",
"patch=1,EE,001435C4,word,04000200",
"patch=1,EE,001435C8,word,08040800",
"patch=1,EE,001435CC,word,08100808",
"patch=1,EE,001435D0,word,00000820",
"patch=1,EE,001435E0,word,30880800",
"patch=1,EE,001435E4,word,1100000F",
"patch=1,EE,001435E8,word,0000102D",
"patch=1,EE,001435EC,word,308803FC",
"patch=1,EE,001435F0,word,2409000C",
"patch=1,EE,001435F4,word,11000004",
"patch=1,EE,001435F8,word,00000000",
"patch=1,EE,001435FC,word,71005004",
"patch=1,EE,00143600,word,240B0029",
"patch=1,EE,00143604,word,016A4823",
"patch=1,EE,00143608,word,292A0010",
"patch=1,EE,0014360C,word,15400002",
"patch=1,EE,00143610,word,00095840",
"patch=1,EE,00143614,word,252B0010",
"patch=1,EE,00143618,word,256B4000",
"patch=1,EE,0014361C,word,000B1C3C",
"patch=1,EE,00143620,word,24020001",
"patch=1,EE,00143624,word,03E00008",
"patch=1,EE,00143628,word,00000000",
"patch=1,EE,0014362C,word,3C0841DF",
"patch=1,EE,00143630,word,3508FFFF",
"patch=1,EE,00143634,word,0008403C",
"patch=1,EE,00143638,word,0104482B",
"patch=1,EE,0014363C,word,080479DA",
"patch=1,EE,00143640,word,0109200B",
"patch=1,EE,00143650,word,08050D55",
"patch=1,EE,00143654,word,240F0001",
"patch=1,EE,001756F4,word,0C050D78",
"patch=1,EE,001756F8,word,00000000",
"patch=1,EE,001756FC,word,10400004",
"patch=1,EE,00175700,word,00000000",
"patch=1,EE,00175704,word,1000004A",
"patch=1,EE,00175708,word,00000000",
"patch=1,EE,0017570C,word,00000000",
"patch=1,EE,001744C8,word,0C050D8B"
]
},
{
"name": "Score Formula (current pop'n)",
"id": "score",
"lines": [
"author=Claude",
"description=COOLありのスコア式を現行ポップンの式に変更: スコア=100000×(COOL×1.0+GREAT×0.7+GOOD×0.4)÷ポップ君総数(小数点以下切り捨て)。",
"// 0x1798C0-0x1798C4: GREATの加算値 500000 → 700000",
"// 0x1798F0-0x1798F4: GOODの加算値 100000 → 400000",
"patch=1,EE,001798C0,word,3C02000A",
"patch=1,EE,001798C4,word,3442AE60",
"patch=1,EE,001798F0,word,3C020006",
"patch=1,EE,001798F4,word,34421A80"
]
},
{
"name": "FREE COOL Default ON",
"id": "freecool",
"lines": [
"author=Claude",
"description=FREEモードのCOOL判定オプションの初期値をONにする(初期化時にOFF(0)を書き込む処理をON(1)に変更)。オプション画面でOFFに切り替えることは従来どおり可能。",
"// 0x19F9F4: sw zero → sw a0(この時点でa0=1)",
"patch=1,EE,0019F9F4,word,AF848CB0"
]
},
{
"name": "Key Beam Length",
"id": "keybeam",
"lines": [
"author=Claude",
"description=キービームの長さを変更する。下端(判定ライン側)は固定のまま上に向かって縮み、グラデーションも縮小される。「長さ」と書いた1行の値(末尾8桁)を下の表の値に書き換えること。初期値は50%。",
"// 長さの値(元の長さ=100%、画面上のビームの高さは元約308px)",
"//    0% = 00000000 (約  0px)",
"//   10% = 0000000A (約 31px)",
"//   20% = 00000014 (約 62px)",
"//   30% = 0000001E (約 92px)",
"//   40% = 00000028 (約123px)",
"//   50% = 00000032 (約154px)",
"//   60% = 0000003C (約185px)",
"//   70% = 00000046 (約216px)",
"//   80% = 00000050 (約246px)",
"//   90% = 0000005A (約277px)",
"//  100% = 00000064 (約308px)",
"// 仕組み: ビームはテクスチャ30x308/24x308のスプライト。スプライト描画関数(0x1382C0)がGSパケットを書き終える箇所(0x138D2C)に",
"//   コードを差し込み、パケットのUV矩形が 幅30or24・高さ308 のとき、上端の頂点Yを「(100-長さ)%」ぶん下げて、下端を動かさずに縮める。",
"//   差し込みコードは空きRAM 0x000FFE00 以降、長さの値は 0x000FFF04 に置く。",
"// 長さ(この1行だけ書き換える)",
"patch=1,EE,000FFF04,word,00000032",
"// ここから下は変更しない",
"patch=1,EE,00138D2C,word,0803FF80",
"patch=1,EE,000FFE00,word,8E4800A0",
"patch=1,EE,000FFE04,word,8E4900D0",
"patch=1,EE,000FFE08,word,01284823",
"patch=1,EE,000FFE0C,word,240A01E0",
"patch=1,EE,000FFE10,word,112A0004",
"patch=1,EE,000FFE14,word,00000000",
"patch=1,EE,000FFE18,word,240A0180",
"patch=1,EE,000FFE1C,word,152A0016",
"patch=1,EE,000FFE20,word,00000000",
"patch=1,EE,000FFE24,word,8E4800A4",
"patch=1,EE,000FFE28,word,8E4900D4",
"patch=1,EE,000FFE2C,word,01284823",
"patch=1,EE,000FFE30,word,240A1340",
"patch=1,EE,000FFE34,word,152A0010",
"patch=1,EE,000FFE38,word,00000000",
"patch=1,EE,000FFE3C,word,8E4800C4",
"patch=1,EE,000FFE40,word,8E4900F4",
"patch=1,EE,000FFE44,word,01284823",
"patch=1,EE,000FFE48,word,1920000B",
"patch=1,EE,000FFE4C,word,00000000",
"patch=1,EE,000FFE50,word,3C0A0010",
"patch=1,EE,000FFE54,word,8D4AFF04",
"patch=1,EE,000FFE58,word,240B0064",
"patch=1,EE,000FFE5C,word,016A5023",
"patch=1,EE,000FFE60,word,012A0018",
"patch=1,EE,000FFE64,word,00005012",
"patch=1,EE,000FFE68,word,014B001A",
"patch=1,EE,000FFE6C,word,00005012",
"patch=1,EE,000FFE70,word,010A4021",
"patch=1,EE,000FFE74,word,AE4800C4",
"patch=1,EE,000FFE78,word,24030010",
"patch=1,EE,000FFE7C,word,0804E34C",
"patch=1,EE,000FFE80,word,00000000"
]
},
{
"name": "Lane Brightness",
"id": "lane",
"lines": [
"comment=Darken the key lane background. Rewrite ONLY the value at 000FFA00 (hex, 00-64):",
"comment=  100%=00000064 (original)  90%=0000005A  80%=00000050  70%=00000046  60%=0000003C",
"comment=   50%=00000032  40%=00000028  30%=0000001E  20%=00000014  10%=0000000A  0%=00000000 (black)",
"comment=Default is 70%. Only the lane background is affected (not notes/beam).",
"patch=1,EE,000FFA00,word,0000000A",
"patch=1,EE,00138D34,word,0803FEC0",
"patch=1,EE,000FFB00,word,AE4000FC",
"patch=1,EE,000FFB04,word,8E4800C0",
"patch=1,EE,000FFB08,word,8E4900C4",
"patch=1,EE,000FFB0C,word,8E4A00F0",
"patch=1,EE,000FFB10,word,8E4B00F4",
"patch=1,EE,000FFB14,word,340C77F0",
"patch=1,EE,000FFB18,word,010C602B",
"patch=1,EE,000FFB1C,word,15800042",
"patch=1,EE,000FFB20,word,00000000",
"patch=1,EE,000FFB24,word,340C6FF0",
"patch=1,EE,000FFB28,word,012C602B",
"patch=1,EE,000FFB2C,word,1580003E",
"patch=1,EE,000FFB30,word,00000000",
"patch=1,EE,000FFB34,word,340C8801",
"patch=1,EE,000FFB38,word,014C602B",
"patch=1,EE,000FFB3C,word,1180003A",
"patch=1,EE,000FFB40,word,00000000",
"patch=1,EE,000FFB44,word,340C8A01",
"patch=1,EE,000FFB48,word,016C602B",
"patch=1,EE,000FFB4C,word,11800036",
"patch=1,EE,000FFB50,word,00000000",
"patch=1,EE,000FFB54,word,01487823",
"patch=1,EE,000FFB58,word,2DEC0F60",
"patch=1,EE,000FFB5C,word,15800032",
"patch=1,EE,000FFB60,word,00000000",
"patch=1,EE,000FFB64,word,2DEC0F61",
"patch=1,EE,000FFB68,word,1180002F",
"patch=1,EE,000FFB6C,word,00000000",
"patch=1,EE,000FFB70,word,0169C023",
"patch=1,EE,000FFB74,word,2F0C1000",
"patch=1,EE,000FFB78,word,1580002B",
"patch=1,EE,000FFB7C,word,00000000",
"patch=1,EE,000FFB80,word,2F0C1501",
"patch=1,EE,000FFB84,word,11800028",
"patch=1,EE,000FFB88,word,00000000",
"patch=1,EE,000FFB8C,word,3C0C0010",
"patch=1,EE,000FFB90,word,8D8CFA00",
"patch=1,EE,000FFB94,word,240D0064",
"patch=1,EE,000FFB98,word,8E4800B0",
"patch=1,EE,000FFB9C,word,010C0018",
"patch=1,EE,000FFBA0,word,00004012",
"patch=1,EE,000FFBA4,word,010D001A",
"patch=1,EE,000FFBA8,word,00004012",
"patch=1,EE,000FFBAC,word,AE4800B0",
"patch=1,EE,000FFBB0,word,8E4800B4",
"patch=1,EE,000FFBB4,word,010C0018",
"patch=1,EE,000FFBB8,word,00004012",
"patch=1,EE,000FFBBC,word,010D001A",
"patch=1,EE,000FFBC0,word,00004012",
"patch=1,EE,000FFBC4,word,AE4800B4",
"patch=1,EE,000FFBC8,word,8E4800B8",
"patch=1,EE,000FFBCC,word,010C0018",
"patch=1,EE,000FFBD0,word,00004012",
"patch=1,EE,000FFBD4,word,010D001A",
"patch=1,EE,000FFBD8,word,00004012",
"patch=1,EE,000FFBDC,word,AE4800B8",
"patch=1,EE,000FFBE0,word,8E4800E0",
"patch=1,EE,000FFBE4,word,010C0018",
"patch=1,EE,000FFBE8,word,00004012",
"patch=1,EE,000FFBEC,word,010D001A",
"patch=1,EE,000FFBF0,word,00004012",
"patch=1,EE,000FFBF4,word,AE4800E0",
"patch=1,EE,000FFBF8,word,8E4800E4",
"patch=1,EE,000FFBFC,word,010C0018",
"patch=1,EE,000FFC00,word,00004012",
"patch=1,EE,000FFC04,word,010D001A",
"patch=1,EE,000FFC08,word,00004012",
"patch=1,EE,000FFC0C,word,AE4800E4",
"patch=1,EE,000FFC10,word,8E4800E8",
"patch=1,EE,000FFC14,word,010C0018",
"patch=1,EE,000FFC18,word,00004012",
"patch=1,EE,000FFC1C,word,010D001A",
"patch=1,EE,000FFC20,word,00004012",
"patch=1,EE,000FFC24,word,AE4800E8",
"patch=1,EE,000FFC28,word,0804E34E",
"patch=1,EE,000FFC2C,word,00000000"
]
},
{
"name": "Judge Adjust 4ms Step",
"id": "jstep",
"lines": [
"author=Claude",
"description=判定調整を4ms刻みにする。元は1段階=約16ms(1単位=4msの4倍)。このパッチでは内部の設定値の1段階=4ms(元の1/4)にし、設定画面の操作範囲を内部値-60〜+60(=表示-15〜+15のまま、±240ms)に広げる。表示は「内部値÷4(0方向に切り捨て)」なので、見た目は今まで通り整数のみ(内部が-2なら表示0、-6なら表示-1)。左右ボタン1回で4ms動き、表示は4回ごとに変わる。",
"// 仕組み(popn14): 設定値は符号付き1バイト(保存先0x01A53AF4、設定画面中は0x0024FC3C)。",
"//   0x174B20/0x174B34/0x17BE44: ゲーム内で設定値に掛ける倍率を ×4 → ×1 に(1単位=4ms)",
"//   0x1E46B0/0x1E46BC/0x1E4784/0x1E4790: 設定画面の範囲(元は-15〜+15で端を越えると反対側へ)を-60〜+60に",
"//   0x1E3BF8 → 0x000FFD00: 設定画面の表示用に設定値を読む命令を、÷4(0方向切り捨て)して返す短いコードに差し替え",
"// 注意: この4msパッチを入れる前に保存した設定値(-15〜+15)は、内部値として読まれるため効果が1/4に見える。設定画面で入れ直すこと。",
"patch=1,EE,00174B20,word,00021000",
"patch=1,EE,00174B34,word,00021000",
"patch=1,EE,0017BE44,word,00021800",
"patch=1,EE,001E46B0,word,2841FFC4",
"patch=1,EE,001E46BC,word,2402003C",
"patch=1,EE,001E4784,word,2841003D",
"patch=1,EE,001E4790,word,2402FFC4",
"patch=1,EE,001E3BF8,word,0803FF40",
"patch=1,EE,000FFD00,word,838390CC",
"patch=1,EE,000FFD04,word,00030FC3",
"patch=1,EE,000FFD08,word,00010F82",
"patch=1,EE,000FFD0C,word,00611821",
"patch=1,EE,000FFD10,word,08078F00",
"patch=1,EE,000FFD14,word,00031883"
]
},
{
"name": "COOL Window 25ms",
"id": "coolwin",
"lines": [
"author=Claude",
"description=COOL判定の幅を±16ms(内部値±4)から現行ポップンの±25ms(内部値±6)に広げる。判定結果を決める処理の中で「時間差が-4以上かつ4以下ならCOOL」と比較している即値(-4と5)を(-6と7)に書き換えるだけで、GREAT以下の判定幅とスコア式は変えない。",
"// 内部の時間単位は1/240秒(約4.17ms)。COOL ±4=±16.7ms → ±6=±25.0ms。",
"// このタイトルのGREAT幅は内部値±12(約±50.0ms)なので、COOL ±6はGREATの内側に収まる。",
"// 幅を変えたい場合: 「-4」の行の末尾4桁を(-N)の16ビット値、「5」の行の末尾4桁を(N+1)に書き換える。",
"//   N=4(元)  FFFC / 0005    N=5  FFFB / 0006    N=6(25ms)  FFFA / 0007    N=7  FFF9 / 0008",
"// 「-4」の行は slti(時間差 < -N)、「5」の行は slti(時間差 < N+1)。「-4」の行が2つあるタイトルは、分岐の遅延スロットに入った同じ比較の複製(両方書き換える)。",
"patch=1,EE,00179E2C,word,2A22FFFA",
"patch=1,EE,00179E38,word,2A210007"
]
},
{
"name": "480p Test (experimental)",
"id": "p480",
"lines": [
"author=Claude",
"comment=実験用。起動時にゲームを最初から起動すること（ステートのロードでは反映されない）。sceGsResetGraph を 480i→480p(inter=0, omode=0x50, ffmd=1) に変更し、毎フレームの DISPLAY 定数を 480p 用(DX=440 DY=35 MAGH=2倍 DW=1023 DH=447)にする。512幅のまま出力するため、PCSX2 側でアスペクト比を 4:3 にして使う。",
"patch=1,EE,00142560,word,24050000",
"patch=1,EE,00142564,word,24060050",
"patch=1,EE,0014256C,word,24070001",
"patch=1,EE,0014304C,word,3463F3FF",
"patch=1,EE,00143054,word,3C030082",
"patch=1,EE,00143058,word,346431B8",
"patch=1,EE,0014305C,word,346331B8"
]
}
]
},
"SLPM-62288_098E1539": {
"gametitle": "gametitle=pop'n music Best Hits! (CRC 098E1539)",
"sections": [
{
"name": "HiSpeed x2-x8 with .5 steps",
"id": "hispeed",
"lines": [
"author=Claude",
"comment=OFF→2→2.5→…→7.5→8→OFF。表示は.5が元の段階、x5→x2, x6→x3, x7/x8→x4（曲選択画面のHI-SPEEDラベルも同じ表示）",
"patch=1,EE,00131350,word,0000482D",
"patch=1,EE,00131354,word,1080000B",
"patch=1,EE,00131358,word,24830003",
"patch=1,EE,0013135C,word,00031842",
"patch=1,EE,00131360,word,24630002",
"patch=1,EE,00131364,word,24090001",
"patch=1,EE,00131368,word,00694804",
"patch=1,EE,0013136C,word,30830001",
"patch=1,EE,00131370,word,14600004",
"patch=1,EE,00131374,word,00000000",
"patch=1,EE,00131378,word,35290800",
"patch=1,EE,0013137C,word,00000000",
"patch=1,EE,00131380,word,00000000",
"patch=1,EE,0013130C,word,000322C2",
"patch=1,EE,00131310,word,30840001",
"patch=1,EE,00131314,word,306307F0",
"patch=1,EE,00131318,word,10600005",
"patch=1,EE,0013131C,word,0000102D",
"patch=1,EE,00131320,word,2482FFF7",
"patch=1,EE,00131324,word,00031842",
"patch=1,EE,00131328,word,1460FFFE",
"patch=1,EE,0013132C,word,24420002",
"patch=1,EE,00131330,word,03E00008",
"patch=1,EE,00131334,word,00000000",
"patch=1,EE,00131338,word,3C01EAA5",
"patch=1,EE,0013133C,word,34210A50",
"patch=1,EE,00131340,word,00031840",
"patch=1,EE,00131344,word,00611806",
"patch=1,EE,00131348,word,30630003",
"patch=1,EE,0013134C,word,080502A0",
"patch=1,EE,0012FDB4,word,2862000D",
"patch=1,EE,0012FE30,word,8F838268",
"patch=1,EE,0012FE34,word,0C04C4CE",
"patch=1,EE,0012FE38,word,00000000",
"patch=1,EE,0012FE3C,word,3C020018",
"patch=1,EE,0012FE40,word,00431021",
"patch=1,EE,0012FE44,word,8C45E900",
"patch=1,EE,0012FF78,word,8F838268",
"patch=1,EE,0012FF7C,word,0C04C4CE",
"patch=1,EE,0012FF80,word,2463FFFF",
"patch=1,EE,0012FF84,word,3C020018",
"patch=1,EE,0012FF88,word,00431021",
"patch=1,EE,0012FF8C,word,8C45E900",
"patch=1,EE,0014A850,word,30620090",
"patch=1,EE,0014A858,word,30620120",
"patch=1,EE,0014A884,word,30620640",
"patch=1,EE,00140A38,word,308307F0",
"patch=1,EE,00140A3C,word,1060000D",
"patch=1,EE,00140A40,word,24023FF0",
"patch=1,EE,00140A44,word,00042AC2",
"patch=1,EE,00140A48,word,30A50001",
"patch=1,EE,00140A4C,word,24A5FFFA",
"patch=1,EE,00140A50,word,00031842",
"patch=1,EE,00140A54,word,1460FFFE",
"patch=1,EE,00140A58,word,24A50002",
"patch=1,EE,00140A5C,word,28A30008",
"patch=1,EE,00140A60,word,10600003",
"patch=1,EE,00140A64,word,00051040",
"patch=1,EE,00140A68,word,00051080",
"patch=1,EE,00140A6C,word,2442FFF0",
"patch=1,EE,00140A70,word,24424000",
"patch=1,EE,00140A74,word,00021C3C",
"patch=1,EE,00140A78,word,10000005",
"patch=1,EE,00140A7C,word,FF838378",
"patch=1,EE,00140A80,word,03E00008",
"patch=1,EE,00140A84,word,00031880",
"patch=1,EE,00140A88,word,00000000",
"patch=1,EE,00140A8C,word,00000000",
"patch=1,EE,00130570,word,8F838268",
"patch=1,EE,00130574,word,0C04C4CE",
"patch=1,EE,00130578,word,2463FFFF",
"patch=1,EE,0013057C,word,2402000C",
"patch=1,EE,00130580,word,1062003E",
"patch=1,EE,00130584,word,00035082",
"patch=1,EE,00130588,word,24020010",
"patch=1,EE,0013058C,word,3C0400BA",
"patch=1,EE,00130590,word,FFA20000",
"patch=1,EE,00130594,word,24070064",
"patch=1,EE,00130598,word,24842000",
"patch=1,EE,0013059C,word,FFA00008",
"patch=1,EE,001305A0,word,24030005",
"patch=1,EE,001305A4,word,FFA40010",
"patch=1,EE,001305A8,word,3C02000E",
"patch=1,EE,001305AC,word,FFA30018",
"patch=1,EE,001305B0,word,34440022",
"patch=1,EE,001305B4,word,008A2021",
"patch=1,EE,001305B8,word,2405000A",
"patch=1,EE,001305BC,word,24060182",
"patch=1,EE,001305C0,word,00E0402D",
"patch=1,EE,001305C4,word,0000482D",
"patch=1,EE,001305C8,word,0000502D",
"patch=1,EE,001305CC,word,0C049B1C",
"patch=1,EE,001305D0,word,0200582D",
"patch=1,EE,001305D4,word,10000029",
"patch=1,EE,001305D8,word,00000000"
]
},
{
"name": "Judge Timing Adjust",
"id": "jtime",
"lines": [
"author=Claude",
"description=判定タイミング調整。最後の行の下4桁(XXXX)が調整値(16ビット符号付き、判定の内部単位)。0000=調整なし／FFFF=-1／FFFE=-2／FFFC=-4／FFF8=-8／0001=+1／0002=+2／0004=+4。マイナス=判定ラインが遅くなる(遅めに押してもジャスト)、プラス=判定ラインが早くなる。上4桁(24A5)と他の行は変更しないこと。ベストヒッツは時刻をスタック経由で渡すため、判定走査ループの戻り先を1語前にずらして時刻を読み直し、調整値を加算している(判定処理に渡す時刻だけをずらすので譜面表示と音はそのまま)。",
"patch=1,EE,001443EC,word,1440FFE0",
"patch=1,EE,00144370,word,8FA5004C",
"patch=1,EE,00144374,word,24A5FFF8"
]
},
{
"name": "COOL Judge in All Modes",
"id": "coolall",
"lines": [
"author=Claude",
"description=全モードでCOOL判定を有効化(GREAT範囲の中心±4でCOOL)し、スコア計算をCOOLありの式にする(ただしGOODは0点ではなく100000)。COOLのゲージ増加量はGREATと同じ(ゲージの仕様は各モードのまま)。オートプレイ/デモもCOOLになる。画面下のカウンター欄を全モードでCOOL付きにする(フレームは各モードのまま)。",
"// 0x143F08: COOL判定の条件を常に成立",
"// 0x143820: COOL判定の結果を全モードで処理(元はCOOLなしでは無視)",
"// 0x14385C: COOL時のゲージ増減にGREATの値を使う",
"// 0x144234: オートプレイのCOOL条件を常に成立",
"// 0x144698: スコア満点を全モードでCOOLありの式に(ノーツ数x10)",
"// 0x143BF8/0x143C24/0x143C44-0x143C54: スコア加算をCOOLありの式に(COOL=1000000/GREAT=500000)し、GOODを追加(100000、元のCOOLなしの加算処理を流用)",
"// 0x13ABC4/0x13ABD4: 画面下のカウンター欄の重ね画像を全モードでCOOL付き(0x90017)に",
"// 0x13A6F0: 画面下の表示部品を常にCOOLありの形で作成",
"// 0x134268: リザルト画面を通常版(0x1358A0)の代わりにCOOL付き版(0x134A90)で初期化",
"// 0x134388/0x1343AC/0x1343E4: リザルト画像の読み込みも通常版(0x135D10)からCOOL付き版(0x135080)に差し替え(初期化だけ差し替えると画像が無く崩れる)",
"patch=1,EE,0013A6F0,word,00000000",
"patch=1,EE,0013ABC4,word,34A30017",
"patch=1,EE,0013ABD4,word,34700017",
"patch=1,EE,00143820,word,00000000",
"patch=1,EE,0014385C,word,24040000",
"patch=1,EE,00143BF8,word,00000000",
"patch=1,EE,00143C24,word,16200007",
"patch=1,EE,00143C44,word,3A210001",
"patch=1,EE,00143C48,word,10200006",
"patch=1,EE,00143C4C,word,00000000",
"patch=1,EE,00143C50,word,10000009",
"patch=1,EE,00143C54,word,00000000",
"patch=1,EE,00143F08,word,00000000",
"patch=1,EE,00144234,word,00000000",
"patch=1,EE,00144698,word,00000000",
"patch=1,EE,00134268,word,10600010",
"patch=1,EE,00134388,word,0C04D420",
"patch=1,EE,001343AC,word,0C04D420",
"patch=1,EE,001343E4,word,0C04D420"
]
},
{
"name": "Score Formula (current pop'n)",
"id": "score",
"lines": [
"author=Claude",
"description=COOLありのスコア式を現行ポップンの式に変更: スコア=100000×(COOL×1.0+GREAT×0.7+GOOD×0.4)÷ポップ君総数(小数点以下切り捨て)。[COOL Judge in All Modes]と一緒に有効にすること。",
"// 0x143C30-0x143C34: GREATの加算値 500000 → 700000",
"// 0x143C68-0x143C6C: GOODの加算値 100000 → 400000",
"patch=1,EE,00143C30,word,3C02000A",
"patch=1,EE,00143C34,word,3442AE60",
"patch=1,EE,00143C68,word,3C020006",
"patch=1,EE,00143C6C,word,34421A80"
]
},
{
"name": "No FEVER at Gauge MAX",
"id": "nofever",
"lines": [
"author=Claude",
"description=ゲージMAX時にGREATがFEVER表示になるのを無効化し、常に通常のGREATとして表示する(スコアは元からGREATと同じ扱いなので変化なし)。キャラクターのアニメーションは変更しない。",
"// 0x143898: FEVER判定の分岐を常に通常GREAT側へ",
"patch=1,EE,00143898,word,1000000A"
]
},
{
"name": "Key Beam Length",
"id": "keybeam",
"lines": [
"author=Claude",
"description=キービームの長さを変更する。下端(判定ライン側)は固定のまま上に向かって縮み、グラデーションも縮小される。「長さ」と書いた2行の値(末尾8桁)を下の表の同じ値に書き換えること。初期値は50%。",
"// 長さの値(2行とも同じ値にする。元の長さ=100%、ビームの高さは元257px)",
"//     0% = 00000000 (  0px)",
"//    10% = 0000000A ( 25px)",
"//    20% = 00000014 ( 51px)",
"//    30% = 0000001E ( 77px)",
"//    40% = 00000028 (102px)",
"//    50% = 00000032 (128px)",
"//    60% = 0000003C (154px)",
"//    70% = 00000046 (179px)",
"//    80% = 00000050 (205px)",
"//    90% = 0000005A (231px)",
"//   100% = 00000064 (257px)",
"// 仕組み: ビームはスプライトセット0のフレーム150-153(テクスチャ30x257)。キーフレーム0x9A2410-0x9A2608(間隔0x48)の",
"//   基準点Yとオフセットトラックの Y を257(スプライト下端)にし、Yスケールのトラックを空きRAMに置いた新しいトラックに差し替える。",
"//   0x000FFF00 = 幅100%のビーム用(横100%、縦=値)、0x000FFF10 = 幅80%のビーム用(横80%、縦=値)",
"// 次の5か所がプレイ画面のスプライトセットの値と一致するときだけ書き込む(Eコード。リザルト等の別画面では書き込まない)",
"//   0xB9D204=40C0(セット0のデータ位置) / 0x9A2412=0096(フレーム番号) / 0x9A2420=000F(基準点X) / 0x99F54A=000F / 0x99F622=000C(トラックX)",
"patch=1,EE,E02C40C0,extended,00B9D204",
"patch=1,EE,E02B0096,extended,009A2412",
"patch=1,EE,E02A000F,extended,009A2420",
"patch=1,EE,E029000F,extended,0099F54A",
"patch=1,EE,E028000C,extended,0099F622",
"// 長さ(幅100%のビーム)",
"patch=1,EE,200FFF04,extended,00000032",
"// 長さ(幅80%のビーム)",
"patch=1,EE,200FFF14,extended,00000032",
"// ここから下は変更しない",
"patch=1,EE,200FFF00,extended,00640000",
"patch=1,EE,200FFF08,extended,0000FFFF",
"patch=1,EE,200FFF0C,extended,00000000",
"patch=1,EE,200FFF10,extended,00500000",
"patch=1,EE,200FFF18,extended,0000FFFF",
"patch=1,EE,200FFF1C,extended,00000000",
"patch=1,EE,209A2428,extended,FF762D00",
"patch=1,EE,209A24B8,extended,FF762D00",
"patch=1,EE,209A2548,extended,FF762D00",
"patch=1,EE,209A25D8,extended,FF762D00",
"patch=1,EE,209A2470,extended,FF762D10",
"patch=1,EE,209A2500,extended,FF762D10",
"patch=1,EE,209A2590,extended,FF762D10",
"patch=1,EE,209A2620,extended,FF762D10",
"patch=1,EE,109A2422,extended,00000101",
"patch=1,EE,109A24B2,extended,00000101",
"patch=1,EE,109A2542,extended,00000101",
"patch=1,EE,109A25D2,extended,00000101",
"patch=1,EE,109A246A,extended,00000101",
"patch=1,EE,109A24FA,extended,00000101",
"patch=1,EE,109A258A,extended,00000101",
"patch=1,EE,109A261A,extended,00000101",
"patch=1,EE,1099F54C,extended,00000101",
"patch=1,EE,1099F554,extended,00000101",
"patch=1,EE,1099F564,extended,00000101",
"patch=1,EE,1099F56C,extended,00000101",
"patch=1,EE,1099F58C,extended,00000101",
"patch=1,EE,1099F594,extended,00000101",
"patch=1,EE,1099F5A4,extended,00000101",
"patch=1,EE,1099F5AC,extended,00000101",
"patch=1,EE,1099F5CC,extended,00000101",
"patch=1,EE,1099F5D4,extended,00000101",
"patch=1,EE,1099F5E4,extended,00000101",
"patch=1,EE,1099F5EC,extended,00000101",
"patch=1,EE,1099F60C,extended,00000101",
"patch=1,EE,1099F614,extended,00000101",
"patch=1,EE,1099F624,extended,00000101",
"patch=1,EE,1099F62C,extended,00000101"
]
},
{
"name": "Lane Brightness",
"id": "lane",
"lines": [
"comment=Darken the key lane background. Rewrite ONLY the value at 000FFA00 (hex, 00-64):",
"comment=  100%=00000064 (original)  90%=0000005A  80%=00000050  70%=00000046  60%=0000003C",
"comment=   50%=00000032  40%=00000028  30%=0000001E  20%=00000014  10%=0000000A  0%=00000000 (black)",
"comment=Default is 70%. Only the lane background is affected (not notes/beam).",
"patch=1,EE,000FFA00,word,00000046",
"patch=1,EE,00125800,word,0803FEC0",
"patch=1,EE,000FFB00,word,ADC000CC",
"patch=1,EE,000FFB04,word,8DC80090",
"patch=1,EE,000FFB08,word,8DC90094",
"patch=1,EE,000FFB0C,word,8DCA00C0",
"patch=1,EE,000FFB10,word,8DCB00C4",
"patch=1,EE,000FFB14,word,340C77F0",
"patch=1,EE,000FFB18,word,010C602B",
"patch=1,EE,000FFB1C,word,1580003B",
"patch=1,EE,000FFB20,word,00000000",
"patch=1,EE,000FFB24,word,340C6FF0",
"patch=1,EE,000FFB28,word,012C602B",
"patch=1,EE,000FFB2C,word,15800037",
"patch=1,EE,000FFB30,word,00000000",
"patch=1,EE,000FFB34,word,340C87A1",
"patch=1,EE,000FFB38,word,014C602B",
"patch=1,EE,000FFB3C,word,11800033",
"patch=1,EE,000FFB40,word,00000000",
"patch=1,EE,000FFB44,word,340C83D1",
"patch=1,EE,000FFB48,word,016C602B",
"patch=1,EE,000FFB4C,word,1180002F",
"patch=1,EE,000FFB50,word,00000000",
"patch=1,EE,000FFB54,word,01487823",
"patch=1,EE,000FFB58,word,2DEC07C0",
"patch=1,EE,000FFB5C,word,1580002B",
"patch=1,EE,000FFB60,word,00000000",
"patch=1,EE,000FFB64,word,2DEC07C1",
"patch=1,EE,000FFB68,word,11800028",
"patch=1,EE,000FFB6C,word,00000000",
"patch=1,EE,000FFB70,word,3C0C0010",
"patch=1,EE,000FFB74,word,8D8CFA00",
"patch=1,EE,000FFB78,word,240D0064",
"patch=1,EE,000FFB7C,word,8DC80080",
"patch=1,EE,000FFB80,word,010C0018",
"patch=1,EE,000FFB84,word,00004012",
"patch=1,EE,000FFB88,word,010D001A",
"patch=1,EE,000FFB8C,word,00004012",
"patch=1,EE,000FFB90,word,ADC80080",
"patch=1,EE,000FFB94,word,8DC80084",
"patch=1,EE,000FFB98,word,010C0018",
"patch=1,EE,000FFB9C,word,00004012",
"patch=1,EE,000FFBA0,word,010D001A",
"patch=1,EE,000FFBA4,word,00004012",
"patch=1,EE,000FFBA8,word,ADC80084",
"patch=1,EE,000FFBAC,word,8DC80088",
"patch=1,EE,000FFBB0,word,010C0018",
"patch=1,EE,000FFBB4,word,00004012",
"patch=1,EE,000FFBB8,word,010D001A",
"patch=1,EE,000FFBBC,word,00004012",
"patch=1,EE,000FFBC0,word,ADC80088",
"patch=1,EE,000FFBC4,word,8DC800B0",
"patch=1,EE,000FFBC8,word,010C0018",
"patch=1,EE,000FFBCC,word,00004012",
"patch=1,EE,000FFBD0,word,010D001A",
"patch=1,EE,000FFBD4,word,00004012",
"patch=1,EE,000FFBD8,word,ADC800B0",
"patch=1,EE,000FFBDC,word,8DC800B4",
"patch=1,EE,000FFBE0,word,010C0018",
"patch=1,EE,000FFBE4,word,00004012",
"patch=1,EE,000FFBE8,word,010D001A",
"patch=1,EE,000FFBEC,word,00004012",
"patch=1,EE,000FFBF0,word,ADC800B4",
"patch=1,EE,000FFBF4,word,8DC800B8",
"patch=1,EE,000FFBF8,word,010C0018",
"patch=1,EE,000FFBFC,word,00004012",
"patch=1,EE,000FFC00,word,010D001A",
"patch=1,EE,000FFC04,word,00004012",
"patch=1,EE,000FFC08,word,ADC800B8",
"patch=1,EE,000FFC0C,word,08049601",
"patch=1,EE,000FFC10,word,00000000"
]
},
{
"name": "COOL Window 25ms",
"id": "coolwin",
"lines": [
"author=Claude",
"description=COOL判定の幅を±16ms(内部値±4)から現行ポップンの±25ms(内部値±6)に広げる。判定結果を決める処理の中で「時間差が-4以上かつ4以下ならCOOL」と比較している即値(-4と5)を(-6と7)に書き換えるだけで、GREAT以下の判定幅とスコア式は変えない。",
"// 内部の時間単位は1/240秒(約4.17ms)。COOL ±4=±16.7ms → ±6=±25.0ms。",
"// このタイトルのGREAT幅は内部値±8(約±33.3ms)なので、COOL ±6はGREATの内側に収まる。",
"// 幅を変えたい場合: 「-4」の行の末尾4桁を(-N)の16ビット値、「5」の行の末尾4桁を(N+1)に書き換える。",
"//   N=4(元)  FFFC / 0005    N=5  FFFB / 0006    N=6(25ms)  FFFA / 0007    N=7  FFF9 / 0008",
"// 「-4」の行は slti(時間差 < -N)、「5」の行は slti(時間差 < N+1)。「-4」の行が2つあるタイトルは、分岐の遅延スロットに入った同じ比較の複製(両方書き換える)。",
"patch=1,EE,00143F10,word,2A42FFFA",
"patch=1,EE,00143F1C,word,2A410007"
]
},
{
"name": "480p Test (experimental)",
"id": "p480",
"lines": [
"author=Claude",
"comment=実験用。起動時にゲームを最初から起動すること（ステートのロードでは反映されない）。sceGsResetGraph を 480i→480p(inter=0, omode=0x50, ffmd=1) に変更し、480i のフィールド描画用の SCANMSK を常に 0 にする。BEST HITS は SDK が 480p 非対応のため DISPLAY をコードケイブで設定する。512幅のまま出力するため、PCSX2 側でアスペクト比を 4:3 にして使う。",
"patch=1,EE,00129678,word,24050000",
"patch=1,EE,0012967C,word,24060050",
"patch=1,EE,00129684,word,24070001",
"patch=1,EE,00100650,word,0803FD80",
"patch=1,EE,00100654,word,00000000",
"patch=1,EE,000FF600,word,3C02001B",
"patch=1,EE,000FF604,word,3442F3FF",
"patch=1,EE,000FF608,word,0002103C",
"patch=1,EE,000FF60C,word,3C030082",
"patch=1,EE,000FF610,word,346331B8",
"patch=1,EE,000FF614,word,00431025",
"patch=1,EE,000FF618,word,FE220018",
"patch=1,EE,000FF61C,word,08040196",
"patch=1,EE,000FF620,word,00000000",
"patch=1,EE,001289D8,word,24020000",
"patch=1,EE,00177D90,word,00000000",
"patch=1,EE,00177E10,word,00000000"
]
}
]
}
}''')

UNIT_PER_SEC = 240.0   # 判定の内部時間単位 1/240 秒


# --------------------------------------------------------------------------
# 多言語 (日本語 / English)
# --------------------------------------------------------------------------
LANG = "ja"


def T(ja, en):
    return en if LANG == "en" else ja


def default_lang():
    try:
        import locale
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            loc = locale.getdefaultlocale()[0] or ""
        return "en" if loc and not loc.lower().startswith("ja") else "ja"
    except Exception:  # noqa
        return "ja"


# 機能名・説明・数値欄の英語表記（日本語は各機能クラスの定義を使う）
FEAT_EN = {
    "coolwin": ("Set COOL window to \u00b125ms",
                "Makes the COOL window \u00b125ms (original \u00b116.7ms). COOL is only judged inside the GREAT window, so it cannot be wider than GREAT."),
    "keybeam": ("Key beam length",
                "Length of the key beam as a percentage of the original. The bottom stays fixed and the top shrinks."),
    "lane": ("Lane background brightness",
             "Brightness of the key lane background (100% = original, 0% = black). Notes and beams are unaffected."),
    "jtime": ("Judge timing adjustment",
              "Shifts only the time passed to judging (chart display and audio are unchanged). Negative = judge line later / positive = earlier. 7-12 and BEST HITS only."),
    "hispeed": ("Extended hi-speed",
                "Extends the hi-speed choices (x8-x10 / .5 steps; contents differ by title)."),
    "coolall": ("COOL judgment in all modes",
                "Enables COOL in every mode and matches scoring / result display to COOL-enabled play. 7-12 / BEST HITS."),
    "score": ("Current pop'n score formula",
              "Score = 100000 x (COOL x 1.0 + GREAT x 0.7 + GOOD x 0.4) / total pop-kuns."),
    "nofever": ("No FEVER display at max gauge", ""),
    "perfect": ("PERFECT = GOOD 0 and BAD 0", "10-12 only."),
    "freecool": ("FREE COOL default ON", "13 / 14 only."),
    "jstep": ("Judge adjustment in 4ms steps",
              "13 / 14 only. Note: previously saved offset values must be re-entered."),
    "barline": ("Bar lines OFF", "Do not draw bar lines (8 only)."),
    "defchara": ("Default character on the select screen",
                 "Changes the character selected first on the character select screen (7 / 8 / 9 / BEST HITS). "
                 "For characters not in the list, type a hex ID such as 0x15. Tick the 2P box for the 2P colour (ID+1; ignored for characters without one). Behaviour with locked characters is unverified. "
                 "Boot the game from scratch (loading a save state does not apply it)."),
    "p480": ("480p output (experimental)",
             "Outputs 480p at 512 width. Set the PCSX2 aspect ratio to 4:3 and boot the game from scratch. "
             "7/9/10/11 are unverified; BEST HITS blackout during loading is unverified."),
}
PARAM_EN = {("keybeam", "pct"): ("Length", "%"), ("lane", "pct"): ("Brightness", "%"),
            ("jtime", "units"): ("Offset", "units (~4ms)")}
GROUP_EN = {"システム関連": "System", "COOL 関連": "COOL", "オプション関連": "Options", "その他": "Other"}


def fname(f):
    return FEAT_EN[f.id][0] if LANG == "en" and f.id in FEAT_EN else f.name


def fnote(f):
    return FEAT_EN[f.id][1] if LANG == "en" and f.id in FEAT_EN else f.note


def plabel(f, p):
    return PARAM_EN[(f.id, p[0])][0] if LANG == "en" and (f.id, p[0]) in PARAM_EN else p[1]


def punit(f, p):
    return PARAM_EN[(f.id, p[0])][1] if LANG == "en" and (f.id, p[0]) in PARAM_EN else p[6]


def gname(g):
    return GROUP_EN.get(g, g) if LANG == "en" else g


# --------------------------------------------------------------------------
# 機能定義
# --------------------------------------------------------------------------
class Feature:
    id = ""
    name = ""
    order = 0
    params = []          # [(key, label, min, max, default, step, unit)]
    note = ""

    def section_for(self, serial):
        for s in DATA[serial]["sections"]:
            if s["id"] == self.id:
                return s
        return None

    def supported(self, serial):
        return self.section_for(serial) is not None

    def titles_label(self):
        return ""

    def build(self, serial, p):
        """-> (セクション名, [行])  行は '//'・description=・patch= を含む"""
        s = self.section_for(serial)
        return s["name"], list(s["lines"])


class Verbatim(Feature):
    def __init__(self, id, name, order, note=""):
        self.id, self.name, self.order, self.note = id, name, order, note


def _sub_value(line, newval):
    """patch 行の末尾の値(16進)を newval に置換（桁数は維持）"""
    m = re.match(r"^(patch=\d,EE,[0-9A-Fa-f]{8},\w+,)([0-9A-Fa-f]+)$", line)
    w = len(m.group(2))
    return m.group(1) + ("%0*X" % (w, newval & ((1 << (4 * w)) - 1)))


class CoolWindow(Feature):
    id, name, order = "coolwin", "COOL 判定幅を ±25ms にする", 12
    note = ("判定結果が COOL になる時間差を ±25ms にします（元は ±16.7ms）。"
            "COOL は GREAT の範囲内でだけ判定されるため、GREAT より広くはなりません。")

    def build(self, serial, p):
        n = 6      # 25ms = 6 単位 (1/240s)
        out = []
        for l in self.section_for(serial)["lines"]:
            m = re.match(r"^patch=\d,EE,[0-9A-Fa-f]{8},word,2A..([0-9A-F]{4})$", l)
            if m:
                low = int(m.group(1), 16)
                # 負の即値(-N) = slti 下限 / 正の即値(N+1) = 上限
                out.append(_sub_value(l, (-n if low >= 0x8000 else n + 1) & 0xFFFF | (int(l[-8:], 16) & 0xFFFF0000)))
            elif l.startswith("patch="):
                raise ValueError("COOL Window: 想定外の行 %s" % l)
        eff = n * 1000.0 / UNIT_PER_SEC
        lines = ["author=popn_modernize_patcher",
                 "description=COOL 判定幅を内部値 +-%d (1/240s) = +-%.1fms にする。slti の即値だけを書き換える。" % (n, eff)] + out
        return "COOL Window %dms" % round(eff), lines


class KeyBeam(Feature):
    id, name, order = "keybeam", "キービーム長", 21
    params = [("pct", "長さ", 0, 100, 50, 5, "%")]
    note = "キービームの長さ（元の長さに対する割合）。下端は固定で上側が縮みます。"

    def build(self, serial, p):
        v = int(round(p["pct"]))
        s = self.section_for(serial)
        out, hit = [], 0
        for l in s["lines"]:
            if re.match(r"^patch=\d,EE,[02]00FFF(04|14),\w+,[0-9A-Fa-f]{8}$", l, re.I):
                l = _sub_value(l, v)
                hit += 1
            out.append(l)
        if hit == 0:
            raise ValueError("Key Beam: 値の行が見つかりません (%s)" % serial)
        return s["name"], out


class LaneBrightness(Feature):
    id, name, order = "lane", "レーン裏の明度", 22
    params = [("pct", "明度", 0, 100, 70, 5, "%")]
    note = "鍵盤レーン背景の明るさ（100%=元の明るさ, 0%=黒）。ノーツ・ビームは変わりません。"

    def build(self, serial, p):
        v = int(round(p["pct"]))
        s = self.section_for(serial)
        out, hit = [], 0
        for l in s["lines"]:
            if re.match(r"^patch=\d,EE,000FFA00,word,[0-9A-Fa-f]{8}$", l, re.I):
                l = _sub_value(l, v)
                hit += 1
            out.append(l)
        if hit != 1:
            raise ValueError("Lane Brightness: 値の行が不正 (%s)" % serial)
        return s["name"], out


class JudgeTiming(Feature):
    id, name, order = "jtime", "判定タイミング調整", 2
    params = [("units", "調整値", -32, 32, -8, 1, "単位 (≈4ms)")]
    note = ("判定に渡す時刻だけをずらします（譜面表示・音は変わらない）。"
            "マイナス=判定ラインが遅くなる / プラス=早くなる。7〜12 と BEST HITS のみ。")

    def build(self, serial, p):
        v = int(round(p["units"]))
        s = self.section_for(serial)
        lines = list(s["lines"])
        idx = max(i for i, l in enumerate(lines) if l.startswith("patch="))   # 最後の patch 行が調整値
        m = re.match(r"^(patch=\d,EE,[0-9A-Fa-f]{8},word,)([0-9A-Fa-f]{4})([0-9A-Fa-f]{4})$", lines[idx])
        lines[idx] = m.group(1) + m.group(2) + "%04X" % (v & 0xFFFF)
        return s["name"], lines


class Barline(Feature):
    id, name, order = "barline", "小節線 OFF", 4
    note = "小節線を描画しない（8 のみ）。"


class P480(Feature):
    id, name, order = "p480", "480p 出力（実験的）", 5
    note = ("512 幅のまま 480p で出力。PCSX2 のアスペクト比を 4:3 に。ゲームは最初から起動すること。"
            "7/9/10/11 は未確認、BEST HITS はロード中の暗転が未確認。")


class ExtraFeature(Feature):
    def __init__(self, d):
        self.id, self.name, self.order = d["id"], d["name"], 50
        self.section, self.note = d.get("section", d["name"]), d.get("description", "")
        if d.get("name_en") or d.get("description_en"):
            FEAT_EN[self.id] = (d.get("name_en", self.name), d.get("description_en", self.note))
        pr = d.get("param")
        self.params = [("value", pr.get("label", "値"), pr["min"], pr["max"], pr["default"],
                        pr.get("step", 1), pr.get("unit", ""))] if pr else []
        self.titles = d["titles"]

    def section_for(self, serial):
        return {"name": self.section} if serial in self.titles else None

    def build(self, serial, p):
        v = p.get("value", 0)
        if self.params and float(self.params[0][5]).is_integer():
            v = int(round(v))
        return self.section, ["author=popn_modernize_patcher"] + [t.format(value=v) for t in self.titles[serial]]


# --------------------------------------------------------------------------
# キャラ選択の初期キャラ (Default Character)
# --------------------------------------------------------------------------
# 既存 pnach の [Default Character] から抽出: {serial: (元の既定ID, [(アドレス, 命令上位16bit)])}
# 値は  命令上位16bit + ID(4桁16進)  = MIPS の addiu 即値  (例: 2402 0006 = addiu v0,zero,6)
CHARA_PATCH = {
    "SLPM-62288_098E1539": (0x00, [("0015F970", "2402"), ("001600A4", "2406"), ("00160648", "2402"), ("00160A04", "2402")]),
    "SLPM-65208_459970FC": (0x11, [("0012D2E0", "2402"), ("0012D570", "2402")]),
    "SLPM-65316_18B64A1A": (0x17, [("0012A370", "2402"), ("001A6000", "2402")]),
    "SLPM-65508_DFBAFDE3": (0x80, [("00137D8C", "2402"), ("00138A34", "2402"), ("00156404", "2402"),
                                   ("001A492C", "2403"), ("001ABAE4", "2402")]),
}

# タイトルごとのキャラ表 {serial: [(ID, 名前)]} (chara_data.json の ID + popnfever のキャラ一覧の日本語名)。
# 名前末尾の * は解禁条件あり(8 / BEST HITS)。(n) は登場バージョン。9 は内部ラベルからの対応づけで画面表示と異なる場合がある。
# 名前を特定できなかったキャラは内部名(英語)のまま。
# アプリと同じフォルダの characters.json で追加・上書きできる:
#   {"SLPM-65316_18B64A1A": [{"id": 27, "name": "BAMBOO"}, {"id": "0x17", "name": "MARY"}]}
CHARA_TABLES = {
    'SLPM-65208_459970FC': [(0, 'ディーノ'), (2, 'ワルドック'), (4, 'ユリちゃん'), (7, 'レイヴガール'), (9, 'さなえちゃん'), (11, 'ナナ'), (13, 'ニャミ'), (15, 'ミミ'), (17, 'マリィ'), (19, 'キング'), (21, 'バンブー'), (23, 'セバスちゃん'), (25, 'ペペ'), (27, 'かごめ'), (29, 'ヤンヤン'), (31, 'ジュディ'), (33, 'サンディ'), (35, 'サイバー'), (37, 'プリンスM'), (39, 'ポエット'), (41, 'ユンタ'), (43, 'ジズ'), (45, 'テルオ'), (47, 'プリティ'), (49, 'ピータン'), (51, 'シャラ'), (53, 'ウォーカー'), (55, 'ニナ'), (57, 'リエちゃん'), (59, 'ムラサキ'), (61, 'ナンシー'), (63, 'ヨシオ'), (65, 'マック'), (67, 'リゼット'), (69, 'クッキー'), (71, 'アッシュ'), (73, 'MZD'), (100, 'ヴァンテーン(CS)'), (102, 'アゲハ'), (104, 'さなえちゃん'), (106, 'ハマノフ'), (108, 'ボゥイ'), (110, 'アンズ'), (112, 'ウオヲ'), (114, 'トロッピー'), (116, 'ディック'), (118, 'ジュディ'), (120, 'ショルキー'), (122, 'ミリィ'), (124, 'ドラゴン'), (126, 'ミミ'), (128, 'ロマ'), (130, 'ファットボーイ'), (132, 'ザ・モッキー'), (134, 'いぬ千代'), (136, 'ムツキ'), (138, 'レイチェル'), (140, 'ライカーズ'), (144, 'W.B.ローズ'), (146, 'アゲハ'), (148, 'ふき'), (150, 'スミレ'), (152, 'シルヴィー'), (154, 'ジョルジュ&エバ'), (156, '小山明美'), (158, 'ヒグラシ'), (160, 'マッチュッチュ'), (162, 'キャンディ'), (164, 'ケリー'), (166, 'P-1&P-2'), (168, 'ヴァンテーン'), (170, 'もえ'), (172, 'ミミ(スタディ)'), (174, 'ニャミ(スタディ)')],
    'SLPM-65316_18B64A1A': [(5, 'MZD'), (7, 'プリンスM'), (9, 'ユンタ'), (11, 'シャラ'), (13, 'アッシュ'), (15, 'さなえちゃん'), (17, 'レイヴガール'), (19, 'ニャミ'), (21, 'ミミ'), (23, 'マリィ'), (25, 'キング'), (27, 'バンブー'), (29, 'ニュー・ミュー'), (30, 'ニュー・ミュー(2)'), (31, 'パピルス'), (33, 'モモコさん'), (35, 'ロビン&クック *'), (37, 'シノビアン'), (39, 'TEMPULA2002'), (41, 'リエちゃん'), (43, 'MUYU'), (45, 'JIG'), (47, 'トルマリン'), (49, 'YAQ'), (51, 'EEL'), (53, 'PSY'), (55, 'PUNK'), (57, 'WALTS'), (59, 'アルト'), (61, 'UKULELE'), (63, 'TAKA'), (65, 'さなえちゃん *'), (67, 'RETRO'), (71, 'SHOWYA'), (73, 'ユーリ'), (75, 'リゼット'), (77, 'アッシュ'), (79, 'ししゃも'), (81, 'NAOKI'), (103, 'ハマノフ'), (104, 'ボウイ *'), (105, 'ROMANCE KAYOU *'), (106, 'トロッピー *'), (107, 'HOUSE MIMI *'), (108, 'BOA *'), (109, 'SCAT *'), (110, 'SF GIRL *'), (111, 'アヤ *'), (112, 'ジュライ *'), (113, 'WALL *'), (114, 'SALSA *'), (115, 'DDR *'), (116, 'MANHATTAN *'), (117, 'ウサおくん *'), (118, 'リサ *'), (119, 'MOBOMOGA *'), (120, 'CASSANDRA *'), (121, 'JET *'), (122, 'テクノスターズ *'), (123, 'LINUS *'), (124, 'ANUBIS *'), (125, 'BeiLei'), (127, 'エル'), (129, 'グリーン'), (131, 'ハマノフ'), (133, 'ヒグラシ'), (135, 'アイス'), (137, '小山明美 *'), (139, 'リナ'), (141, 'メイファ *'), (143, 'マコト *'), (145, 'マリィ'), (147, 'マチルダ *'), (149, 'むぎばたけ *'), (151, 'ポール'), (153, 'スクーリオン'), (155, 'サニー'), (157, '睦月'), (159, 'るり'), (161, 'ライカーズ'), (163, 'アゲハ'), (165, 'ふき'), (167, 'もえ'), (169, '小山明美'), (171, 'ミミ(スタディ)')],
    'SLPM-65508_DFBAFDE3': [(0, 'アニー'), (2, 'イワン'), (4, 'IKKEI_10A'), (6, 'ウオヲ'), (8, 'ウパ'), (10, 'エマ'), (12, 'MZD(9)'), (14, 'エル(4)'), (16, 'オリビア(1)'), (18, 'オリビア(5)'), (20, 'カゲトラ'), (22, 'かごめ'), (24, 'キララ'), (26, 'キャンディ'), (28, 'クラフト(1)'), (30, 'クルミ'), (32, 'ケビン'), (34, 'コービー'), (36, 'ロビン&クック'), (38, '小山明美'), (40, 'さなえちゃん(5)'), (42, 'さなえちゃん(8)'), (44, 'さなえちゃん(9)'), (46, 'サニー'), (48, 'ジェフ'), (50, 'ジズ(9)'), (52, 'ジュディ(5)'), (54, 'ジュディ(8)'), (56, 'ジュディ(9)'), (58, 'シルビア'), (60, 'シルヴェスター'), (62, 'ソウジ'), (64, 'チャーリー'), (66, 'ツララ'), (68, 'カミカゼトオル'), (70, 'MC.トメ'), (72, 'トラン(6)'), (74, 'トラン(9)'), (76, 'ニナ(9)'), (78, 'ニャミ(6)'), (80, 'ニャミ(9)'), (82, 'ナン'), (84, 'ハマノフ(8)'), (86, 'ハヤト'), (88, 'P-1&P-2(3)'), (90, 'Bis子'), (92, 'ジングウヒロシ'), (94, 'フォース'), (96, 'フォクシー(10)'), (98, 'ブロンソン'), (100, 'ベル(9)'), (102, 'ヘンリー'), (104, 'ポエット(3)'), (106, 'ポエット(4)'), (108, 'ポエット(9)'), (110, 'ホセ'), (112, 'ポッパーズ(9)'), (114, 'BoB 2002'), (116, 'マコト'), (118, 'マチルダ'), (120, 'マッチュッチュ'), (122, 'マリィ(9)'), (124, 'ミサキ(10)'), (126, 'むぎばたけ'), (128, 'ミミ(9)'), (130, 'メイ・ファ'), (132, 'メメ'), (134, 'ヨシオ'), (136, 'リエちゃん(9)'), (138, 'リゼット(7)'), (140, 'レイヴガール(4)'), (142, '六(6)'), (144, '六(9)'), (146, 'アリス'), (148, 'マリィ(7)'), (150, 'エル(8)'), (152, 'テトラ'), (154, 'シャーク'), (156, 'モリー vs スーツ'), (158, 'ジャガー・B'), (160, 'ポト'), (162, 'ハマノフ(9)'), (164, 'ルーシー'), (166, 'ハロン'), (168, 'ロビッツ'), (170, 'ヒュー'), (172, 'プリティ(CS)'), (174, '翼'), (176, 'トビーズ'), (178, 'るり'), (180, 'ホシオ'), (182, 'ポエット(7)'), (184, 'キリ'), (186, 'アッシュ(7)'), (188, 'アゲハ'), (190, 'スミレ'), (192, 'ななことそらまめ'), (194, 'B・ボーン先生'), (195, 'MZD_OKINAWA'), (196, 'MZD_HITEN'), (197, 'MZD_MELOW'), (198, 'MZD_SHOWA'), (199, '009'), (200, 'OBAQ'), (201, 'CATS'), (202, 'ホネニャミ'), (203, 'COMPUTER'), (204, 'YOSHIMOTO'), (205, 'LOBSTER'), (206, 'ユキ(4)'), (207, 'ユキ(4) B'), (208, 'ミミ(5)'), (209, 'ミミ(5) B'), (210, 'エドワード'), (211, 'エドワード B'), (212, 'ユリちゃん'), (213, 'ユリちゃん B'), (214, 'カップくん'), (215, 'ワルドック'), (216, 'ワルドック B')],
    'SLPM-62288_098E1539': [(0, 'ニャミ a1'), (2, 'ミミ a1'), (4, 'マリィ a1'), (6, 'キング a1'), (8, 'リエちゃん a1'), (10, 'リエちゃん a4s *'), (12, 'ジャムおじさん a1'), (14, 'バンブー a1'), (16, 'ニャミ a2'), (18, 'ミミ a2'), (20, 'マリィ a2'), (22, 'キング a2'), (24, 'ジュディ a2'), (26, 'スギくん a2'), (28, 'レオくん a5 *'), (30, 'タイマー a2'), (32, 'ユーリ c2'), (34, 'シンディ c2'), (36, 'ケリー c2'), (38, 'メイ・ファ c2'), (40, 'ニャミ a3'), (42, 'ミミ a3'), (44, 'マリィ a3'), (46, 'キング a3'), (48, 'リンリン a3'), (50, 'ボゥイ c2'), (52, 'ニャミ a4'), (54, 'ミミ a4'), (56, 'マリィ a4'), (58, 'キング a4'), (60, 'ジュディ a4'), (62, 'ポエット a4'), (64, 'ユーリ a4'), (66, 'さなえちゃん a4'), (68, 'アッシュ a4'), (70, 'アイス a4'), (72, 'スマイル a4'), (74, 'アントニオ c4'), (76, 'ハマノフ c2'), (78, 'ニャミ a5'), (80, 'ミミ a5'), (82, 'マリィ a5'), (84, 'キング a5'), (86, 'Mr.ケーケー a5'), (88, 'ショルキー a5'), (90, 'ジュディ a5'), (92, 'ワッキー a5'), (94, 'ベル a5'), (96, 'さなえちゃん a5 *'), (98, 'リエちゃん a5'), (100, 'スペース・マコ a5'), (102, 'アッシュ a5'), (104, 'ニャミ a6'), (106, 'ミミ a6'), (108, 'マリィ a6'), (110, 'キング a6'), (112, 'バンブー a6'), (114, '六 a6'), (116, 'トラン a6'), (118, 'スミレ c6'), (120, 'おとこマン a6'), (122, 'タイマー a6'), (124, 'アゲハ c5'), (126, 'ウオヲ c6'), (128, 'ＭＺＤ a7 *'), (130, 'プリティ cB1 *'), (132, 'アンズ cB1 *'), (134, 'ボゥイ cB1 *'), (136, 'リデル cB1 *'), (138, 'ニコ cB1')],
}


# 2P カラー(ID+1)を持たないキャラ: 次の ID が別キャラとして存在するもの (chara_data.json から算出)
CHARA_NO2P = {
    'SLPM-65208_459970FC': set([6, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 106, 107, 108, 109, 142, 143]),
    'SLPM-65316_18B64A1A': set([29, 30, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]),
    'SLPM-65508_DFBAFDE3': set([194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215]),
    'SLPM-62288_098E1539': set([]),
}

def _to_id(v):
    if isinstance(v, int):
        return v
    return int(str(v).strip(), 16 if str(v).strip().lower().startswith("0x") else 10)


def load_chara_tables():
    """内蔵キャラ表 + characters.json -> ({serial: [(id, name)]}, エラー文字列 or None)"""
    tables = {s: list(t) for s, t in CHARA_TABLES.items()}
    path = os.path.join(APP_DIR, "characters.json")
    err = None
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                for serial, rows in json.load(f).items():
                    if serial not in CHARA_PATCH:
                        continue
                    cur = dict(tables.get(serial, []))
                    for r in rows:
                        cur[_to_id(r["id"])] = str(r["name"])
                    tables[serial] = sorted(cur.items())
        except Exception as e:  # noqa
            err = T("characters.json の読み込みに失敗: %s", "Failed to load characters.json: %s") % e
    CHARA_TABLES.update(tables)   # DefaultChara.build の説明文でも同じ表を使う
    return tables, err


def chara_label(cid, name):
    return "0x%02X  %s" % (cid, name) if name else "0x%02X" % cid


def parse_chara(text, table):
    """コンボボックスの文字列 -> ID。'0x15  BAMBOO' / '0x15' / '21' / 'BAMBOO' を受け付ける。不正なら ValueError"""
    t = (text or "").strip()
    m = re.match(r"^0x([0-9A-Fa-f]{1,4})(\s|$)", t)
    if m:
        return int(m.group(1), 16)
    for cid, nm in table:
        if t and t.lower() == nm.lower():
            return cid
    if re.match(r"^[0-9]{1,5}$", t) and int(t) <= 0xFFFF:
        return int(t)
    raise ValueError(t)


class DefaultChara(Feature):
    id, name, order = "defchara", "キャラ選択の初期キャラを変更", 30
    note = ("キャラクター選択画面で最初に選ばれているキャラを変更します（7 / 8 / 9 / BEST HITS）。"
            "リストにないキャラは 0x15 のような16進IDを直接入力できます。「2P」にチェックすると2Pカラー（ID+1）になります（2Pカラーのないキャラでは無視）。未解禁キャラの挙動は未確認。"
            "ゲームは最初から起動すること（ステートのロードでは反映されません）。")

    def section_for(self, serial):
        return {"name": "Default Character"} if serial in CHARA_PATCH else None

    def clean_params(self, pd):
        ch = pd.get("chara") if isinstance(pd.get("chara"), dict) else {}
        out = {}
        for s, (orig, _) in CHARA_PATCH.items():
            try:
                out[s] = min(max(int(ch.get(s, orig)), 0), 0xFFFF)
            except (TypeError, ValueError):
                out[s] = orig
        c2 = pd.get("chara2p") if isinstance(pd.get("chara2p"), dict) else {}
        return {"chara": out, "chara2p": {s: bool(c2.get(s, False)) for s in CHARA_PATCH}}

    def build(self, serial, p):
        orig, rows = CHARA_PATCH[serial]
        cid = int((p.get("chara") or {}).get(serial, orig))
        if not 0 <= cid <= 0xFFFF:
            raise ValueError("Default Character: ID out of range")
        table = dict(CHARA_TABLES.get(serial, []))
        base = cid
        two_p = bool((p.get("chara2p") or {}).get(serial)) and cid not in CHARA_NO2P.get(serial, ()) and cid < 0xFFFF
        if two_p:
            cid += 1   # 2P カラーは 1P の ID + 1
        lines = ["description=キャラクター選択画面の初期キャラを 0x%02X%s%s にする(書き込む値 0x%02X)。元の既定値は 0x%02X%s。"
                 "ゲームを最初から起動すること(ステートのロードでは反映されない)。"
                 % (base, "(%s)" % table[base] if base in table else "", " の2Pカラー" if two_p else "", cid, orig, "(%s)" % table[orig] if orig in table else ""),
                 "// 選択キャラIDの保存値を読み込む命令を、即値の addiu に置換"]
        lines += ["patch=1,EE,%s,word,%s%04X" % (a, pre, cid) for a, pre in rows]
        return "Default Character", lines


FEATURES = [
    CoolWindow(), KeyBeam(), LaneBrightness(), JudgeTiming(), DefaultChara(),
    Verbatim("hispeed", "ハイスピード拡張", 20, "ハイスピードの選択肢を拡張（x8〜x10 / .5 刻み。タイトルにより内容が異なります）。"),
    Verbatim("coolall", "全モードで COOL 判定", 10, "全モードで COOL を有効化し、スコア・リザルト表示も COOL ありに揃える。7〜12 / BEST HITS。"),
    Verbatim("score", "スコア式を現行ポップン化", 1, "スコア=100000×(COOL×1.0+GREAT×0.7+GOOD×0.4)÷ポップ君総数。"),
    Verbatim("nofever", "ゲージ MAX で FEVER 表示にしない", 14),
    Verbatim("perfect", "PERFECT = GOOD 0 & BAD 0", 13, "10〜12 のみ。"),
    Verbatim("freecool", "FREE COOL 初期値 ON", 11, "13 / 14 のみ。"),
    Verbatim("jstep", "判定調整を 4ms 刻みに", 3, "13 / 14 のみ。注意: 保存済みの設定値は入れ直しが必要。"),
    Barline(), P480(),
]


GROUPS = [("システム関連", 0, 9), ("COOL 関連", 10, 19), ("オプション関連", 20, 29), ("その他", 30, 999)]


def group_of(f):
    for nm, lo, hi in GROUPS:
        if lo <= f.order <= hi:
            return nm


def load_extra():
    path = os.path.join(APP_DIR, "features_extra.json")
    out, err = [], None
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                out = [ExtraFeature(d) for d in json.load(f)["features"]]
        except Exception as e:  # noqa
            err = T("features_extra.json の読み込みに失敗: %s", "Failed to load features_extra.json: %s") % e
    return out, err


# --------------------------------------------------------------------------
# pnach の読み書き
# --------------------------------------------------------------------------
SEC_RE = re.compile(r"^\s*\[(.+?)\]\s*$")
NAME_PREFIX = [("HiSpeed", "hispeed"), ("Judge Timing Adjust", "jtime"), ("COOL Judge in All", "coolall"),
               ("Score Formula", "score"), ("No FEVER", "nofever"), ("PERFECT =", "perfect"),
               ("FREE COOL", "freecool"), ("Judge Adjust 4ms", "jstep"), ("Key Beam", "keybeam"),
               ("Lane Brightness", "lane"), ("COOL Window", "coolwin"), ("480p", "p480"), ("Bar Lines", "barline"),
               ("Default Character", "defchara")]


def classify(name):
    for pre, fid in NAME_PREFIX:
        if name.startswith(pre):
            return fid
    return None


def parse_pnach(text):
    header, sections, cur = [], [], None
    for line in text.splitlines():
        m = SEC_RE.match(line)
        if m:
            cur = (m.group(1), [])
            sections.append(cur)
        elif cur is None:
            header.append(line)
        else:
            cur[1].append(line)
    return header, sections


def build_pnach(serial, selected, params, existing_text=None):
    """-> (text, notes, 出力セクション名[])"""
    notes, new = [], []
    for f in selected:
        if not f.supported(serial):
            continue
        name, lines = f.build(serial, params.get(f.id, {}))
        # author は全セクション Claude に統一（既存の author 行は除去して先頭に置く）
        lines = ["author=Claude"] + [l for l in lines if not l.lower().startswith("author=")]
        new.append((f.id, name, lines))
    if existing_text is not None:
        header, old = parse_pnach(existing_text)
        ids = {i for i, _, _ in new}
        kept = []
        for nm, body in old:
            if classify(nm) in ids:
                notes.append(T("既存 [%s] を置き換え", "Replaced existing [%s]") % nm)
            else:
                kept.append((nm, body))
        while header and not header[-1].strip():
            header.pop()
    else:
        header, kept = [DATA[serial]["gametitle"]], []
    out = list(header)
    for nm, body in kept:
        b = list(body)
        while b and not b[-1].strip():
            b.pop()
        out += ["", "[%s]" % nm] + b
    for _, name, lines in sorted(new, key=lambda x: next((f.order for f in selected if f.id == x[0]), 99)):
        out += ["", "[%s]" % name] + lines
    return "\n".join(out) + "\n", notes, [n for _, n, _ in new]


def update_ini(text, new_names, valid_names):
    """gamesettings/<serial>.ini の [Patches] を更新する。
    - valid_names (出力後の pnach に存在するセクション名) に無い Enable 行は削除
    - new_names (今回生成したセクション) の Enable 行を追加
    - [EmuCore/GS] など他のセクション・既存の改行コード (CRLF/LF) は維持
    -> (新しい本文, 追加した名前[], 削除した名前[])"""
    nl = "\r\n" if (text is None or "\r\n" in text) else "\n"
    lines = text.splitlines() if text else []
    # [Patches] セクションの範囲を探す
    start = next((i for i, l in enumerate(lines) if l.strip().lower() == "[patches]"), None)
    if start is None:
        lines = ["[Patches]"] + ([""] + lines if lines else [])
        start = 0
    end = next((i for i in range(start + 1, len(lines)) if SEC_RE.match(lines[i])), len(lines))
    body = lines[start + 1:end]
    enable_re = re.compile(r"^\s*Enable\s*=\s*(.*?)\s*$", re.I)
    valid, kept, removed, present = set(valid_names), [], [], set()
    for l in body:
        m = enable_re.match(l)
        if m:
            nm = m.group(1)
            if nm not in valid:
                removed.append(nm)
                continue
            present.add(nm)
        kept.append(l)
    added = [n for n in new_names if n not in present]
    # 末尾の空行は Enable 行の後ろに回す
    trail = []
    while kept and not kept[-1].strip():
        trail.append(kept.pop())
    kept += ["Enable = %s" % n for n in added] + trail
    out = lines[:start + 1] + kept + lines[end:]
    return nl.join(out) + nl, added, removed



def set_ini_value(text, section, key, value):
    """ini の [section] の key を value にする（無ければ追加）。他の行・改行コードは維持。
    -> (新しい本文, 変更があったか)"""
    nl = "\r\n" if (not text or "\r\n" in text) else "\n"
    lines = text.splitlines() if text else []
    start = next((i for i, l in enumerate(lines) if l.strip().lower() == "[%s]" % section.lower()), None)
    if start is None:
        if lines and lines[-1].strip():
            lines.append("")
        lines += ["[%s]" % section, "%s = %s" % (key, value)]
        return nl.join(lines) + nl, True
    end = next((i for i in range(start + 1, len(lines)) if SEC_RE.match(lines[i])), len(lines))
    kre = re.compile(r"^\s*%s\s*=\s*(.*?)\s*$" % re.escape(key), re.I)
    for i in range(start + 1, end):
        m = kre.match(lines[i])
        if m:
            if m.group(1) == value:
                return nl.join(lines) + nl, False
            lines[i] = "%s = %s" % (key, value)
            return nl.join(lines) + nl, True
    pos = end
    while pos > start + 1 and not lines[pos - 1].strip():
        pos -= 1
    lines.insert(pos, "%s = %s" % (key, value))
    return nl.join(lines) + nl, True


# --------------------------------------------------------------------------
# 設定の保存 / プリセット  (popn_modernize_patcher_settings.json, スクリプトと同じフォルダ)
# --------------------------------------------------------------------------
SETTINGS_PATH = os.path.join(APP_DIR, "popn_modernize_patcher_settings.json")


def load_settings(path=SETTINGS_PATH):
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except Exception:  # noqa  (無い / 壊れている → 初期状態)
        return {}


def save_settings(d, path=SETTINGS_PATH):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def sanitize_config(cfg, features):
    """保存された {features:{id:bool}, params:{id:{key:数値}}} を検証して返す。
    未知の id は無視、数値は範囲内に丸め、欠けた項目は既定値にする。"""
    cfg = cfg if isinstance(cfg, dict) else {}
    fs = cfg.get("features") if isinstance(cfg.get("features"), dict) else {}
    ps = cfg.get("params") if isinstance(cfg.get("params"), dict) else {}
    feats, params = {}, {}
    for f in features:
        feats[f.id] = bool(fs.get(f.id, False))
        pd = ps.get(f.id) if isinstance(ps.get(f.id), dict) else {}
        if hasattr(f, "clean_params"):
            params[f.id] = f.clean_params(pd)
        for key, _label, lo, hi, dflt, _step, _unit in f.params:
            try:
                v = float(pd.get(key, dflt))
            except (TypeError, ValueError):
                v = dflt
            params.setdefault(f.id, {})[key] = min(max(v, lo), hi)
    return feats, params


# --------------------------------------------------------------------------
# GUI
# --------------------------------------------------------------------------
def default_pcsx2_dir():
    for p in (os.path.join(os.path.expanduser("~"), "Documents", "PCSX2"),
              os.path.join(os.path.expanduser("~"), "OneDrive", "Documents", "PCSX2"),
              APP_DIR):
        if os.path.isdir(os.path.join(p, "patches")) or os.path.isdir(os.path.join(p, "gamesettings")):
            return p
    return APP_DIR


def run_gui():
    while _run_gui_once():
        pass


def _run_gui_once():
    """GUI を 1 回構築して実行。言語を切り替えたら True を返し、呼び出し側が作り直す。"""
    global LANG
    LANG = load_settings().get("lang") if load_settings().get("lang") in ("ja", "en") else default_lang()
    restart = [False]
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox, simpledialog

    extra, extra_err = load_extra()
    chara_tables, chara_err = load_chara_tables()
    extra_err = extra_err or chara_err
    features = sorted(FEATURES + extra, key=lambda f: f.order)

    root = tk.Tk()
    root.title(T("pop'n music PS2 pnach ジェネレータ", "pop'n music PS2 pnach generator") + " v" + VERSION)
    root.geometry("1500x860")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # ---- 3 ペイン（境界をドラッグして幅を変更可）: タイトル | 機能 | 出力内容
    paned = ttk.PanedWindow(root, orient="horizontal")
    paned.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

    left = ttk.LabelFrame(paned, text=T("① タイトル（複数選択可）", "1. Titles (multiple allowed)"))
    mid = ttk.LabelFrame(paned, text=T("② 機能（チェックしたものを出力）", "2. Features (checked ones are written)"))
    rightp = ttk.LabelFrame(paned, text=T("③ 出力内容プレビュー", "3. Output preview"))
    paned.add(left, weight=0)
    paned.add(mid, weight=4)
    paned.add(rightp, weight=3)

    title_vars = OrderedDict()
    for nm, serial in TITLES.items():
        v = tk.BooleanVar(value=False)
        title_vars[serial] = v
        ttk.Checkbutton(left, text=nm, variable=v, command=lambda: refresh()).pack(anchor="w", padx=8, pady=3)
    bf = ttk.Frame(left)
    bf.pack(fill="x", padx=8, pady=6)
    lf = ttk.Frame(left)
    lf.pack(side="bottom", fill="x", padx=8, pady=8)
    ttk.Label(lf, text="Language / 言語").pack(anchor="w")
    lang_var = tk.StringVar(value="English" if LANG == "en" else "日本語")
    lang_combo = ttk.Combobox(lf, textvariable=lang_var, values=["日本語", "English"], state="readonly", width=12)
    lang_combo.pack(anchor="w")
    lang_combo.bind("<<ComboboxSelected>>", lambda e: change_lang())
    ttk.Button(bf, text=T("全選択", "Select all"), width=7, command=lambda: [v.set(True) for v in title_vars.values()] or refresh()).pack(side="left")
    ttk.Button(bf, text=T("全解除", "Clear all"), width=7, command=lambda: [v.set(False) for v in title_vars.values()] or refresh()).pack(side="left", padx=4)

    # ---- 機能ペイン（スクロール可・縦いっぱいに表示）
    def set_feats(fs, val):
        for f in fs:
            feat_vars[f.id].set(val)
        refresh()

    hdr = ttk.Frame(mid)
    hdr.pack(side="top", fill="x", padx=8, pady=(4, 0))
    ttk.Label(hdr, text=T("すべての機能:", "All features:")).pack(side="left")
    ttk.Button(hdr, text=T("全選択", "Select all"), width=8, command=lambda: set_feats(features, True)).pack(side="left", padx=4)
    ttk.Button(hdr, text=T("全解除", "Clear all"), width=8, command=lambda: set_feats(features, False)).pack(side="left")
    hdr2 = ttk.Frame(mid)
    hdr2.pack(side="top", fill="x", padx=8, pady=(4, 0))
    ttk.Label(hdr2, text=T("プリセット:", "Preset:")).pack(side="left")
    preset_var = tk.StringVar()
    preset_combo = ttk.Combobox(hdr2, textvariable=preset_var, state="readonly", width=22)
    preset_combo.pack(side="left", padx=4)
    ttk.Button(hdr2, text=T("読込", "Load"), width=6, command=lambda: preset_load()).pack(side="left")
    ttk.Button(hdr2, text=T("保存…", "Save..."), width=7, command=lambda: preset_save()).pack(side="left", padx=2)
    ttk.Button(hdr2, text=T("削除", "Delete"), width=6, command=lambda: preset_delete()).pack(side="left")
    body = ttk.Frame(mid)
    body.pack(side="top", fill="both", expand=True)
    canvas = tk.Canvas(body, highlightthickness=0)
    sb = ttk.Scrollbar(body, orient="vertical", command=canvas.yview)
    inner = ttk.Frame(canvas)
    win = canvas.create_window((0, 0), window=inner, anchor="nw")
    inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda e: canvas.itemconfigure(win, width=e.width))
    canvas.configure(yscrollcommand=sb.set)
    canvas.pack(side="left", fill="both", expand=True)
    sb.pack(side="right", fill="y")
    # ホイールは機能ペイン上にマウスがあるときだけ効かせる
    canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", lambda ev: canvas.yview_scroll(int(-ev.delta / 120), "units")))
    canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

    feat_vars, param_vars, info, chara_vars, chara2p_vars = {}, {}, {}, {}, {}
    wrap_labels = []
    last_group = None
    for f in features:
        g = group_of(f)
        if g != last_group:
            last_group = g
            gh = ttk.Frame(inner)
            gh.pack(fill="x", padx=4, pady=(12, 0))
            ttk.Label(gh, text="[%s]" % gname(g), font=("", 11, "bold")).pack(side="left")
            gfs = [x for x in features if group_of(x) == g]
            ttk.Button(gh, text=T("全選択", "Select all"), width=8, command=lambda gfs=gfs: set_feats(gfs, True)).pack(side="left", padx=(10, 2))
            ttk.Button(gh, text=T("全解除", "Clear all"), width=8, command=lambda gfs=gfs: set_feats(gfs, False)).pack(side="left")
            ttk.Separator(inner).pack(fill="x", padx=4, pady=(2, 0))
        box = ttk.Frame(inner)
        box.pack(fill="x", padx=8, pady=5, anchor="w")
        v = tk.BooleanVar(value=False)
        feat_vars[f.id] = v
        ttk.Checkbutton(box, text=fname(f), variable=v, command=lambda: refresh()).grid(row=0, column=0, sticky="w", columnspan=4)
        param_vars[f.id] = {}
        for i, (key, label, lo, hi, dflt, step, unit) in enumerate(f.params):
            pv = tk.DoubleVar(value=dflt)
            param_vars[f.id][key] = pv
            ttk.Label(box, text=plabel(f, f.params[i])).grid(row=1 + i, column=0, sticky="e", padx=(24, 4))
            ttk.Spinbox(box, from_=lo, to=hi, increment=step, textvariable=pv, width=8).grid(row=1 + i, column=1)
            ttk.Label(box, text=punit(f, f.params[i])).grid(row=1 + i, column=2, sticky="w", padx=4)
            pv.trace_add("write", lambda *a: refresh())
        if f.id == "defchara":   # タイトルごとのキャラ選択（表から選ぶか 0x15 のように直接入力）
            for j, serial in enumerate(CHARA_PATCH):
                o = CHARA_PATCH[serial][0]
                sv = tk.StringVar(value=chara_label(o, dict(chara_tables.get(serial, [])).get(o)))
                chara_vars[serial] = sv
                ttk.Label(box, text=SERIAL_TO_NAME[serial].replace("pop'n music ", "")).grid(row=3 + j, column=0, sticky="e", padx=(24, 4))
                cb = ttk.Combobox(box, textvariable=sv, width=26,
                                  values=[chara_label(c, n) for c, n in chara_tables.get(serial, [])])
                cb.grid(row=3 + j, column=1, columnspan=2, sticky="w")
                bv = tk.BooleanVar(value=False)
                chara2p_vars[serial] = bv
                ttk.Checkbutton(box, text=T("2P カラー", "2P colour"), variable=bv, command=lambda: refresh()).grid(row=3 + j, column=3, sticky="w", padx=6)
                sv.trace_add("write", lambda *a: refresh())
        il = ttk.Label(box, text="", foreground="#a60", justify="left")
        il.grid(row=10, column=0, columnspan=4, sticky="w", padx=24)
        info[f.id] = il
        wrap_labels.append(il)
        if fnote(f):
            nl_ = ttk.Label(box, text=fnote(f), foreground="#777", justify="left")
            nl_.grid(row=11, column=0, columnspan=4, sticky="w", padx=24)
            wrap_labels.append(nl_)
    # 幅に合わせて説明文を折り返す
    canvas.bind("<Configure>", lambda e: (canvas.itemconfigure(win, width=e.width),
                                          [w.config(wraplength=max(200, e.width - 80)) for w in wrap_labels]), add="+")

    # ---- 出力内容ペイン
    preview = tk.Text(rightp, wrap="none", font=("Consolas", 10))
    psy = ttk.Scrollbar(rightp, orient="vertical", command=preview.yview)
    psx = ttk.Scrollbar(rightp, orient="horizontal", command=preview.xview)
    preview.configure(yscrollcommand=psy.set, xscrollcommand=psx.set)
    psy.pack(side="right", fill="y")
    psx.pack(side="bottom", fill="x")
    preview.pack(side="left", fill="both", expand=True)

    # ---- 下部バー: PCSX2 フォルダ / オプション / 出力ボタン
    bottom = ttk.Frame(root)
    bottom.grid(row=1, column=0, sticky="ew", padx=8, pady=(0, 8))
    bottom.columnconfigure(1, weight=1)
    ttk.Label(bottom, text=T("PCSX2 フォルダ", "PCSX2 folder")).grid(row=0, column=0, sticky="e")
    outdir = tk.StringVar(value=default_pcsx2_dir())
    ttk.Entry(bottom, textvariable=outdir).grid(row=0, column=1, sticky="ew", padx=4)
    ttk.Button(bottom, text=T("参照…", "Browse..."), command=lambda: outdir.set(
        (filedialog.askdirectory(title=T("PCSX2 のデータフォルダ (patches / gamesettings の親)", "PCSX2 data folder (parent of patches / gamesettings)")) or outdir.get()).replace("/", os.sep))
    ).grid(row=0, column=2)
    gen_btn = ttk.Button(bottom, text=T("pnach を出力", "Write pnach"))
    gen_btn.grid(row=0, column=3, rowspan=2, padx=(12, 0), sticky="ns")
    merge = tk.BooleanVar(value=True)
    ttk.Checkbutton(bottom, text=T("同名の pnach があれば、チェックしなかった機能のセクションは残して上書き（元ファイルは .bak に退避）", "If a pnach with the same name exists, keep sections of unchecked features and overwrite the rest (original saved as .bak)"),
                    variable=merge).grid(row=1, column=0, columnspan=3, sticky="w")
    enable_ini = tk.BooleanVar(value=True)
    ttk.Checkbutton(bottom, text=T("適用時に PCSX2 側のパッチも有効化する（gamesettings の .ini の [Patches] を更新。元ファイルは .bak に退避）", "Also enable the patches on the PCSX2 side (updates [Patches] in gamesettings .ini; original saved as .bak)"),
                    variable=enable_ini).grid(row=2, column=0, columnspan=3, sticky="w")
    status = tk.StringVar(value=extra_err or "")
    ttk.Label(bottom, textvariable=status, foreground="#a00").grid(row=3, column=0, columnspan=4, sticky="w")

    def sel_serials():
        return [s for s, v in title_vars.items() if v.get()]

    def sel_features():
        return [f for f in features if feat_vars[f.id].get()]

    def get_params():
        out = {}
        for f in features:
            d = {}
            for key, pv in param_vars[f.id].items():
                try:
                    d[key] = pv.get()
                except tk.TclError:
                    d[key] = next(p[4] for p in f.params if p[0] == key)
            if f.id == "defchara":
                d["chara"] = {}
                for serial, sv in chara_vars.items():
                    try:
                        d["chara"][serial] = parse_chara(sv.get(), chara_tables.get(serial, []))
                    except ValueError:
                        d["chara"][serial] = CHARA_PATCH[serial][0]   # 入力が不正なら元の既定値
                d["chara2p"] = {serial: bool(bv.get()) for serial, bv in chara2p_vars.items()}
            out[f.id] = d
        return out

    def refresh():
        params, sers = get_params(), sel_serials()
        for f in features:
            msg = ""
            try:
                if f.id == "jtime":
                    msg = T("→ %+.1f ms 相当", "= %+.1f ms") % (params[f.id]["units"] * 4)
            except Exception:
                pass
            sup = [SERIAL_TO_NAME[s] for s in TITLES.values() if f.supported(s)]
            msg += ("\n" if msg else "") + T("対応: ", "Supported: ") + (", ".join(n.replace("pop'n music ", "") for n in sup) or T("なし", "none"))
            uns = [SERIAL_TO_NAME[s].replace("pop'n music ", "") for s in sers if not f.supported(s)]
            if feat_vars[f.id].get() and uns:
                msg += T("　／　選択中で未対応(スキップ): ", "  /  Unsupported in selection (skipped): ") + ", ".join(uns)
            info[f.id].config(text=msg)
        preview.delete("1.0", "end")
        feats = sel_features()
        if not sers or not feats:
            preview.insert("end", T("タイトルと機能を選ぶとプレビューが表示されます。", "Select titles and features to see the preview."))
            return
        try:
            for s in sers:
                text, _, _ = build_pnach(s, feats, params, None)
                preview.insert("end", "# ===== %s.pnach =====\n%s\n" % (s, text))
        except Exception as e:
            preview.insert("end", T("エラー: %s", "Error: %s") % e)

    def existing_for(serial):
        p = os.path.join(outdir.get(), "patches", serial + ".pnach")
        if merge.get() and os.path.exists(p):
            with open(p, encoding="utf-8", errors="replace") as fh:
                return fh.read()
        return None

    def generate():
        sers, feats = sel_serials(), sel_features()
        if not sers or not feats:
            messagebox.showwarning(T("未選択", "Nothing selected"), T("タイトルと機能を 1 つ以上選んでください。", "Select at least one title and one feature."))
            return
        base = outdir.get()
        if not (os.path.isdir(os.path.join(base, "patches")) or os.path.isdir(os.path.join(base, "gamesettings"))):
            if not messagebox.askyesno(T("確認", "Confirm"), (T("%s に patches / gamesettings フォルダがありません。\n", "%s has no patches / gamesettings folder.\n") +
                                        T("PCSX2 のデータフォルダではない可能性があります。ここに作成して続けますか？", "It may not be a PCSX2 data folder. Create them here and continue?")) % base):
                return
        pdir, gdir = os.path.join(base, "patches"), os.path.join(base, "gamesettings")
        os.makedirs(pdir, exist_ok=True)
        params, log = get_params(), []
        for s in sers:
            old = existing_for(s)
            text, notes, names = build_pnach(s, feats, params, old)
            path = os.path.join(pdir, s + ".pnach")
            if old is not None and not os.path.exists(path + ".bak"):
                with open(path + ".bak", "w", encoding="utf-8", newline="") as fh:
                    fh.write(old)
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
            log.append(T("%s: %d セクション出力", "%s: %d sections written") % (s, len(names)))
            if not enable_ini.get() and any(n.startswith("480p") for n in names):
                log.append(T("   ※ 480p を使うには PCSX2 のゲームプロパティでアスペクト比を 4:3 にしてください",
                             "   * For 480p, set the aspect ratio to 4:3 in the PCSX2 game properties"))
            log += ["   " + n for n in notes]
            if enable_ini.get():
                os.makedirs(gdir, exist_ok=True)
                ipath = os.path.join(gdir, s + ".ini")
                iold = None
                if os.path.exists(ipath):
                    with open(ipath, encoding="utf-8", errors="replace", newline="") as fh:
                        iold = fh.read()
                valid = [n for n, _ in parse_pnach(text)[1]]
                inew, added, removed = update_ini(iold, names, valid)
                # 480p を出力するタイトルは、ゲームプロパティのアスペクト比を 4:3 にする
                aspect = False
                if any(n.startswith("480p") for n in names):
                    inew, aspect = set_ini_value(inew, "EmuCore/GS", "AspectRatio", "4:3")
                if iold is not None and not os.path.exists(ipath + ".bak"):
                    with open(ipath + ".bak", "w", encoding="utf-8", newline="") as fh:
                        fh.write(iold)
                with open(ipath, "w", encoding="utf-8", newline="") as fh:
                    fh.write(inew)
                if aspect:
                    log.append(T("   ini: アスペクト比を 4:3 に設定 (AspectRatio = 4:3)", "   ini: aspect ratio set to 4:3 (AspectRatio = 4:3)"))
                log += [T("   ini 有効化: ", "   ini enabled: ") + n for n in added] + [T("   ini から削除(pnach に無い): ", "   removed from ini (not in pnach): ") + n for n in removed]
        preview.delete("1.0", "end")
        preview.insert("end", "\n".join(log) + "\n\n"
                       + (T("gamesettings の .ini の [Patches] を更新しました。", "Updated [Patches] in the gamesettings .ini.") if enable_ini.get()
                          else T("ini は更新していません（PCSX2 の設定画面でパッチを有効化してください）。", "The ini was not updated (enable the patches in the PCSX2 settings)."))
                       + T("\nPCSX2 の設定 > 詳細 で「パッチを有効にする」(EnablePatches) がオンになっていることも確認してください。", "\nAlso make sure \"Enable Patches\" (EnablePatches) is on in PCSX2 settings > Advanced."))
        status.set(T("出力しました: %s", "Written: %s") % base)
        save_all()

    gen_btn.config(command=generate)

    # ---- 設定の保存・復元 / プリセット
    settings = load_settings()
    presets = settings.get("presets") if isinstance(settings.get("presets"), dict) else {}

    def get_config():
        return {"features": {f.id: bool(feat_vars[f.id].get()) for f in features}, "params": get_params()}

    def apply_config(cfg):
        feats, params = sanitize_config(cfg, features)
        for f in features:
            feat_vars[f.id].set(feats[f.id])
            for k, v in params.get(f.id, {}).items():
                if k == "chara2p":
                    for serial, b in v.items():
                        chara2p_vars[serial].set(b)
                elif k == "chara":
                    for serial, cid in v.items():
                        chara_vars[serial].set(chara_label(cid, dict(chara_tables.get(serial, [])).get(cid)))
                else:
                    param_vars[f.id][k].set(v)
        refresh()

    def save_all(lang=None):
        data = {"lang": lang or LANG, "state": {"titles": sel_serials(), "config": get_config(), "pcsx2_dir": outdir.get(),
                          "merge": bool(merge.get()), "enable_ini": bool(enable_ini.get())},
                "presets": presets}
        try:
            save_settings(data)
        except Exception as e:  # noqa
            status.set(T("設定を保存できませんでした: %s", "Could not save settings: %s") % e)

    def update_preset_list():
        preset_combo["values"] = sorted(presets)

    def preset_load():
        nm = preset_var.get()
        if nm in presets:
            apply_config(presets[nm])
            status.set(T("プリセット「%s」を読み込みました", "Loaded preset '%s'") % nm)

    def preset_save():
        nm = simpledialog.askstring(T("プリセット保存", "Save preset"), T("プリセット名:", "Preset name:"), initialvalue=preset_var.get(), parent=root)
        nm = (nm or "").strip()
        if not nm:
            return
        if nm in presets and not messagebox.askyesno(T("上書き確認", "Confirm overwrite"), T("プリセット「%s」を上書きしますか？", "Overwrite preset '%s'?") % nm):
            return
        presets[nm] = get_config()
        update_preset_list()
        preset_var.set(nm)
        save_all()
        status.set(T("プリセット「%s」を保存しました（機能のチェックと数値。タイトルは含みません）", "Saved preset '%s' (feature checks and values; titles are not included)") % nm)

    def preset_delete():
        nm = preset_var.get()
        if nm in presets and messagebox.askyesno(T("削除確認", "Confirm delete"), T("プリセット「%s」を削除しますか？", "Delete preset '%s'?") % nm):
            del presets[nm]
            preset_var.set("")
            update_preset_list()
            save_all()
            status.set(T("プリセット「%s」を削除しました", "Deleted preset '%s'") % nm)

    def on_close():
        save_all()
        root.destroy()

    def change_lang():
        new = "en" if lang_var.get() == "English" else "ja"
        if new != LANG:
            restart[0] = True
            save_all(new)
            root.destroy()

    update_preset_list()
    st = settings.get("state") if isinstance(settings.get("state"), dict) else {}
    for s in (st.get("titles") if isinstance(st.get("titles"), list) else []):
        if s in title_vars:
            title_vars[s].set(True)
    if isinstance(st.get("pcsx2_dir"), str) and st["pcsx2_dir"]:
        outdir.set(st["pcsx2_dir"])
    if isinstance(st.get("merge"), bool):
        merge.set(st["merge"])
    if isinstance(st.get("enable_ini"), bool):
        enable_ini.set(st["enable_ini"])
    apply_config(st.get("config"))
    root.protocol("WM_DELETE_WINDOW", on_close)
    refresh()
    root.mainloop()
    return restart[0]


def selftest():
    # 既定値で再生成したセクションが、元の pnach と一致することを確認
    for serial, d in DATA.items():
        for f in FEATURES:
            if not f.supported(serial) or f.id == "defchara":
                continue
            orig = f.section_for(serial)
            p = {k: dflt for k, _, _, _, dflt, _, _ in f.params}
            if f.id in ("lane", "keybeam"):
                for l in orig["lines"]:
                    if re.match(r"^patch=.*,(000FFA00|[02]00FFF04),", l, re.I):
                        p["pct"] = int(l[-8:], 16)
            name, lines = f.build(serial, p)
            if f.id == "coolwin":
                a = [l for l in lines if l.startswith("patch=")]
                b = [l for l in orig["lines"] if l.startswith("patch=")]
            else:
                a, b = lines, orig["lines"]
            assert a == b, (serial, f.id, [x for x in zip(a, b) if x[0] != x[1]][:3])
    t, *_ = build_pnach("SLPM-66533_4BD5C7E6", FEATURES, {"keybeam": {"pct": 80},
                                                         "lane": {"pct": 30}, "jtime": {"units": 2}})
    assert "patch=1,EE,00166568,word,2A02FFFA" in t and "patch=1,EE,00166574,word,2A010007" in t, "cool 25ms"
    assert "patch=1,EE,000FFF04,word,00000050" in t and "patch=1,EE,000FFA00,word,0000001E" in t
    t7, *_ = build_pnach("SLPM-65208_459970FC", FEATURES, {"keybeam": {"pct": 20}, "jtime": {"units": 3},
                                                          "lane": {"pct": 70}})
    assert "200FFF04,extended,00000014" in t7 and "200FFF14,extended,00000014" in t7
    assert "patch=1,EE,00161534,word,26450003" in t7
    sample = "[Patches]\r\nEnable = COOL Window 25ms\r\nEnable = HiSpeed x2-x10 with .5 steps\r\nEnable = Old\r\n\r\n\r\n[EmuCore/GS]\r\nAspectRatio = 4:3\r\n"
    out, added, removed = update_ini(sample, ["COOL Window 30ms", "HiSpeed x2-x10 with .5 steps", "Key Beam Length"],
                                     ["COOL Window 30ms", "HiSpeed x2-x10 with .5 steps", "Key Beam Length"])
    assert out == ("[Patches]\r\nEnable = HiSpeed x2-x10 with .5 steps\r\nEnable = COOL Window 30ms\r\nEnable = Key Beam Length\r\n\r\n\r\n"
                   "[EmuCore/GS]\r\nAspectRatio = 4:3\r\n"), repr(out)
    assert added == ["COOL Window 30ms", "Key Beam Length"] and removed == ["COOL Window 25ms", "Old"]
    out2, a2, r2 = update_ini(None, ["X"], ["X"])
    assert out2 == "[Patches]\r\nEnable = X\r\n"
    out3, *_ = update_ini("[EmuCore/GS]\nAspectRatio = 4:3\n", ["X"], ["X"])
    assert out3.startswith("[Patches]\nEnable = X\n") and "AspectRatio = 4:3" in out3, repr(out3)
    # 設定の検証・保存の往復
    class _F:  # noqa
        pass
    cfg = {"features": {"keybeam": True, "bogus": True}, "params": {"keybeam": {"pct": 999}, "lane": {"pct": "x"}}}
    feats, params = sanitize_config(cfg, FEATURES)
    assert feats["keybeam"] is True and feats["lane"] is False and "bogus" not in feats
    assert params["keybeam"]["pct"] == 100 and params["lane"]["pct"] == 70
    assert sanitize_config(None, FEATURES)[0]["coolwin"] is False
    import tempfile
    tp = os.path.join(tempfile.mkdtemp(), "s.json")
    save_settings({"presets": {"a": cfg}}, tp)
    assert load_settings(tp)["presets"]["a"] == cfg and load_settings(tp + ".none") == {}
    s1, c1 = set_ini_value("[Patches]\r\nEnable = X\r\n\r\n[EmuCore/GS]\r\nAspectRatio = Auto 4:3/3:2\r\nCropLeft = 0\r\n", "EmuCore/GS", "AspectRatio", "4:3")
    assert s1 == "[Patches]\r\nEnable = X\r\n\r\n[EmuCore/GS]\r\nAspectRatio = 4:3\r\nCropLeft = 0\r\n" and c1
    s2, c2 = set_ini_value(s1, "EmuCore/GS", "AspectRatio", "4:3")
    assert s2 == s1 and not c2
    s3, _ = set_ini_value("[EmuCore/GS]\nCropLeft = 0\n\n[Other]\na = 1\n", "EmuCore/GS", "AspectRatio", "4:3")
    assert s3 == "[EmuCore/GS]\nCropLeft = 0\nAspectRatio = 4:3\n\n[Other]\na = 1\n", repr(s3)
    s4, _ = set_ini_value("[Patches]\r\nEnable = X\r\n", "EmuCore/GS", "AspectRatio", "4:3")
    assert s4 == "[Patches]\r\nEnable = X\r\n\r\n[EmuCore/GS]\r\nAspectRatio = 4:3\r\n", repr(s4)
    # Default Character: 既存 pnach の値と一致 / 入力解析 / 設定の検証
    dc = DefaultChara()
    n, ls = dc.build("SLPM-62288_098E1539", {"chara": {"SLPM-62288_098E1539": 6}})
    assert n == "Default Character" and "patch=1,EE,001600A4,word,24060006" in ls and "patch=1,EE,0015F970,word,24020006" in ls
    _, ls = dc.build("SLPM-65508_DFBAFDE3", {"chara": {"SLPM-65508_DFBAFDE3": 0x7A}})
    assert "patch=1,EE,001A492C,word,2403007A" in ls and "patch=1,EE,00137D8C,word,2402007A" in ls
    _, ls = dc.build("SLPM-65316_18B64A1A", {"chara": {"SLPM-65316_18B64A1A": 0x1B}})
    assert [l for l in ls if l.startswith("patch=")] == ["patch=1,EE,0012A370,word,2402001B", "patch=1,EE,001A6000,word,2402001B"]
    tb = CHARA_TABLES["SLPM-65208_459970FC"]
    assert parse_chara("0x15  BAMBOO", tb) == 0x15 and parse_chara("バンブー", tb) == 0x15 and parse_chara("19", tb) == 19
    try:
        parse_chara("zzz", tb)
        assert False
    except ValueError:
        pass
    assert not DefaultChara().supported("SLPM-66533_4BD5C7E6") and DefaultChara().supported("SLPM-65208_459970FC")
    _, ls = dc.build("SLPM-65508_DFBAFDE3", {"chara": {"SLPM-65508_DFBAFDE3": 0x7A}, "chara2p": {"SLPM-65508_DFBAFDE3": True}})
    assert "patch=1,EE,00137D8C,word,2402007B" in ls and "patch=1,EE,001A492C,word,2403007B" in ls
    _, ls = dc.build("SLPM-65316_18B64A1A", {"chara": {"SLPM-65316_18B64A1A": 104}, "chara2p": {"SLPM-65316_18B64A1A": True}})
    assert "patch=1,EE,0012A370,word,24020068" in ls   # 2P カラーなしのキャラは +1 しない
    f_, p_ = sanitize_config({"features": {"defchara": True}, "params": {"defchara": {"chara": {"SLPM-65316_18B64A1A": 999999}}}}, FEATURES)
    assert p_["defchara"]["chara"]["SLPM-65316_18B64A1A"] == 0xFFFF and p_["defchara"]["chara"]["SLPM-65208_459970FC"] == 0x11
    print("selftest OK:", sum(len(d["sections"]) for d in DATA.values()), "sections")


if __name__ == "__main__":
    if "--version" in sys.argv:
        print("popn_modernize_patcher v" + VERSION)
    elif "--selftest" in sys.argv:
        selftest()
    else:
        run_gui()
