# ====================
# 学習サイクルの実行
# ====================

# パッケージのインポート
from GameAI.dual_network import dual_network
from GameAI.self_play import self_play
from GameAI.train_network import train_network
from GameAI.evaluate_network import evaluate_network

# デュアルネットワークの作成
dual_network()

for i in range(10):
    print('Train',i,'====================')
    # セルフプレイ部
    self_play()
    # パラメータ更新部
    train_network()
    # 新パラメータ評価部
    evaluate_network()