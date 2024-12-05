def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    all_temperature = [item["temperature"] for item in weather_information]
    total_temperature = sum(all_temperature)
    number_prefecture = len(all_temperature)
    average_temperature = total_temperature / number_prefecture

    print(round(average_temperature, 1))

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    osaka_station = []
    for item in weather_information:
        if item["prefecture"] == "大阪府":
            osaka_station.append(item["station"])

    print(",".join(osaka_station))

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)

    fukuoka_temperature = []
    for item in weather_information:
        if item["prefecture"] == "福岡県":
            fukuoka_temperature.append(item["temperature"])

    total_temperature = sum(fukuoka_temperature)
    number_prefecture = len(fukuoka_temperature)
    fukuoka_temperature = total_temperature / number_prefecture
    print(fukuoka_temperature)


if __name__ == "__main__":
    main()
