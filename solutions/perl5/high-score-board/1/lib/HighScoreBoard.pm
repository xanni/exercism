package HighScoreBoard;

use 5.038;

our %Scores;

sub set_player_scores (%new_scores) {
    return %Scores = ( %Scores, %new_scores );
}

sub get_player_score ($player) {
    return $Scores{$player};
}

sub increase_player_scores (%additional_scores) {
    $Scores{$_} += $additional_scores{$_} foreach keys %additional_scores;
    return;
}

sub sort_players_by_name {
    return sort keys %Scores;
}

sub sort_players_by_score {
    return sort { $Scores{$b} <=> $Scores{$a} } keys %Scores;
}

sub delete_player ($player) {
    return delete $Scores{$player};
}

1;
