def calculate_league_points(wins, draws, losses):
    # Complete this function
    win_points=wins*4
    draw_points=draws*2
    loss_points=losses*-1
    total_points=win_points+loss_points+draw_points
    return total_points


statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
total_points=calculate_league_points(wins, draws, losses)
print(total_points)
# Call the calculate_league_points function
