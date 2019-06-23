from nba_sdk.baseclient import BaseClient, GET

from nba_sdk.request_entities import AssistLeaders, AssistTracker, BoxScoreAdvancedV2, BoxScoreDefensive, \
    BoxScoreFourFactorsV2, BoxScoreMatchups, BoxScoreMiscV2, BoxScorePlayerTrackV2, BoxScoreScoringV2, \
    BoxScoreSummaryV2, BoxScoreTraditionalV2, BoxScoreUsageV2, CommonAllPlayers, CommonPlayerInfo, \
    CommonPlayoffSeries, CommonTeamRoster, CommonTeamYears, DefenseHub, DraftCombineDrillResults, \
    DraftCombineNonStationaryShooting, DraftCombinePlayerAnthro, DraftCombineSpotShooting, DraftCombineStats, \
    DraftHistory, FantasyWidget, FranchiseHistory, FranchiseLeaders, FranchisePlayers, HomePageLeaders, HomePageV2, \
    InfographicFanDuelPlayer, LeadersTiles, LeagueDashLineups, LeagueDashOppPtShot, LeagueDashPlayerBioStats, \
    LeagueDashPlayerClutch, LeagueDashPlayerStats, LeagueDashPtDefend, LeagueDashPtStats, LeagueDashPtTeamDefend, \
    LeagueDashTeamClutch, LeagueDashTeamPtShot, LeagueDashTeamPtStats, LeagueDashTeamShotLocations, LeagueGameFinder, \
    LeagueGameLog, LeagueLeaders, LeaguePlayerOnDetails, LeagueSeasonMatchups, LeagueStandings, PlayByPlayV2, \
    PlayerAwards, PlayerCareerStats, PlayerCompare, PlayerDashboardByClutch, PlayerDashboardByGameSplits, \
    PlayerDashboardByGeneralSplits, PlayerDashboardByLastNGames, PlayerDashboardByOpponent, \
    PlayerDashboardByShootingSplits, PlayerDashboardByTeamPerformance, PlayerDashboardByYearOverYear, \
    PlayerDashPtPass, PlayerDashPtReb, PlayerDashPtShotDefend, PlayerDashPtShots, PlayerFantasyProfile, \
    PlayerFantasyProfileBarGraph, PlayerGameLog, PlayerGameStreakFinder, PlayerNextNGames, PlayerProfileV2, \
    PlayerVsPlayer, PlayoffPicture, Scoreboard, ScoreboardV2, ShotChartDetail, ShotChartLineupDetail, \
    SynergyPlayTypes, TeamAndPlayersVsPlayers, TeamDashboardByClutch, TeamDashboardByGameSplits, \
    TeamDashboardByGeneralSplits, TeamDashboardByLastNGames, TeamDashboardByOpponent, TeamDashboardByShootingSplits, \
    TeamDashboardByTeamPerformance, TeamDashboardByYearOverYear, TeamDashLineups, TeamDashPtPass, TeamDashPtReb, \
    TeamDashPtShots, TeamDetails, TeamGameLog, TeamGameStreakFinder, TeamHistoricalLeaders, TeamInfoCommon, \
    TeamPlayerDashboard, TeamPlayerOnOffDetails, TeamPlayerOnOffSummary, TeamVsPlayer, TeamYearByYearStats, \
    VideoDetails, VideoEvents, VideoStatus
from nba_sdk.utils import build_request

BASE_URL = "https://stats.nba.com/stats"


class NBAStatsClient(BaseClient):
    def __init__(self, **kwargs):
        self._base_url = kwargs.get("base_url", BASE_URL)
        super().__init__()

    @GET
    @build_request
    def assist_leaders(self, assist_leaders=AssistLeaders):
        return assist_leaders

    @GET
    @build_request
    def assist_tracker(self, assist_tracker=AssistTracker):
        return assist_tracker

    @GET
    @build_request
    def boxscore_advancedv2(self, boxscore_advancedv2=BoxScoreAdvancedV2):
        return boxscore_advancedv2

    @GET
    @build_request
    def boxscore_defensive(self, boxscore_defensive=BoxScoreDefensive):
        return boxscore_defensive

    @GET
    @build_request
    def boxscore_fourfactorsv2(self, boxscore_fourfactorsv2=BoxScoreFourFactorsV2):
        return boxscore_fourfactorsv2

    @GET
    @build_request
    def boxscore_matchups(self, boxscore_matchups=BoxScoreMatchups):
        return boxscore_matchups
    
    @GET
    @build_request
    def boxscore_miscv2(self, boxscore_miscv2=BoxScoreMiscV2):
        return boxscore_miscv2
    
    @GET
    @build_request
    def boxscore_playertrackv2(self, boxscore_playertrackv2=BoxScorePlayerTrackV2):
        return boxscore_playertrackv2
    
    @GET
    @build_request
    def boxscore_scoringv2(self, boxscore_scoringv2=BoxScoreScoringV2):
        return boxscore_scoringv2
    
    @GET
    @build_request
    def boxscore_summaryv2(self, boxscore_summaryv2=BoxScoreSummaryV2):
        return boxscore_summaryv2
    
    @GET
    @build_request
    def boxscore_traditionalv2(self, boxscore_traditionalv2=BoxScoreUsageV2):
        return boxscore_traditionalv2
    
    @GET
    @build_request
    def boxscore_usagev2(self, boxscore_usagev2=BoxScoreTraditionalV2):
        return boxscore_usagev2

    @GET
    @build_request
    def common_all_players(self, common_all_players=CommonAllPlayers):
        return common_all_players

    @GET
    @build_request
    def common_player_info(self, common_player_info=CommonPlayerInfo):
        return common_player_info

    @GET
    @build_request
    def common_playoff_series(self, common_playoff_series=CommonPlayoffSeries):
        return common_playoff_series

    @GET
    @build_request
    def common_team_roster(self, common_team_roster=CommonTeamRoster):
        return common_team_roster

    @GET
    @build_request
    def common_team_years(self, common_team_years=CommonTeamYears):
        return common_team_years

    @GET
    @build_request
    def defense_hub(self, defense_hub=DefenseHub):
        return defense_hub

    @GET
    @build_request
    def draft_combine_drill_results(self, draft_combine_drill_results=DraftCombineDrillResults):
        return draft_combine_drill_results

    @GET
    @build_request
    def draft_combine_nonstationary_shooting(
            self, draft_combine_nonstationary_shooting=DraftCombineNonStationaryShooting):
        return draft_combine_nonstationary_shooting

    @GET
    @build_request
    def draft_combine_player_anthro(self, draft_combine_player_anthro=DraftCombinePlayerAnthro):
        return draft_combine_player_anthro

    @GET
    @build_request
    def draft_combine_spot_shooting(self, draft_combine_spot_shooting=DraftCombineSpotShooting):
        return draft_combine_spot_shooting

    @GET
    @build_request
    def draft_combine_stats(self, draft_combine_stats=DraftCombineStats):
        return draft_combine_stats

    @GET
    @build_request
    def draft_history(self, draft_history=DraftHistory):
        return draft_history

    @GET
    @build_request
    def fantasy_widget(self, fantasy_widget=FantasyWidget):
        return fantasy_widget

    @GET
    @build_request
    def franchise_history(self, franchise_history=FranchiseHistory):
        return franchise_history

    @GET
    @build_request
    def franchise_leaders(self, franchise_leaders=FranchiseLeaders):
        return franchise_leaders

    @GET
    @build_request
    def franchise_players(self, franchise_players=FranchisePlayers):
        return franchise_players

    @GET
    @build_request
    def homepage_leaders(self, homepage_leaders=HomePageLeaders):
        return homepage_leaders

    @GET
    @build_request
    def homepagev2(self, homepagev2=HomePageV2):
        return homepagev2

    @GET
    @build_request
    def infographic_fanduel_player(self, infographic_fanduel_player=InfographicFanDuelPlayer):
        return infographic_fanduel_player

    @GET
    @build_request
    def leaders_tiles(self, leaders_tiles=LeadersTiles):
        return leaders_tiles

    @GET
    @build_request
    def leaguedash_lineups(self, leaguedash_lineups=LeagueDashLineups):
        return leaguedash_lineups

    @GET
    @build_request
    def leaguedash_opp_pt_shot(self, leaguedash_opp_pt_shot=LeagueDashOppPtShot):
        return leaguedash_opp_pt_shot

    @GET
    @build_request
    def leaguedash_player_biostats(self, leaguedash_player_biostats=LeagueDashPlayerBioStats):
        return leaguedash_player_biostats

    @GET
    @build_request
    def leaguedash_player_clutch(self, leaguedash_player_clutch=LeagueDashPlayerClutch):
        return leaguedash_player_clutch

    @GET
    @build_request
    def leaguedash_players_stats(self, leaguedash_players_stats=LeagueDashPlayerStats):
        return leaguedash_players_stats

    @GET
    @build_request
    def leaguedash_pt_defend(self, leaguedash_pt_defend=LeagueDashPtDefend):
        return leaguedash_pt_defend

    @GET
    @build_request
    def leaguedash_pt_stats(self, leaguedash_pt_stats=LeagueDashPtStats):
        return leaguedash_pt_stats

    @GET
    @build_request
    def leaguedash_pt_team_defend(self, leaguedash_pt_team_defend=LeagueDashPtTeamDefend):
        return leaguedash_pt_team_defend

    @GET
    @build_request
    def leaguedash_team_clutch(self, leaguedash_team_clutch=LeagueDashTeamClutch):
        return leaguedash_team_clutch

    @GET
    @build_request
    def leaguedash_team_pt_shot(self, leaguedash_team_pt_shot=LeagueDashTeamPtShot):
        return leaguedash_team_pt_shot

    @GET
    @build_request
    def leaguedash_team_pt_stats(self, leaguedash_team_pt_stats=LeagueDashTeamPtStats):
        return leaguedash_team_pt_stats

    @GET
    @build_request
    def leaguedash_team_shot_locations(self, leaguedash_team_shot_locations=LeagueDashTeamShotLocations):
        return leaguedash_team_shot_locations

    @GET
    @build_request
    def league_gamefinder(self, league_gamefinder=LeagueGameFinder):
        return league_gamefinder

    @GET
    @build_request
    def league_gamelog(self, league_gamelog=LeagueGameLog):
        return league_gamelog

    @GET
    @build_request
    def league_leaders(self, league_leaders=LeagueLeaders):
        return league_leaders

    @GET
    @build_request
    def league_playeron_details(self, league_playeron_details=LeaguePlayerOnDetails):
        return league_playeron_details

    @GET
    @build_request
    def league_season_matchups(self, league_season_matchups=LeagueSeasonMatchups):
        return league_season_matchups

    @GET
    @build_request
    def league_standings(self, league_standings=LeagueStandings):
        return league_standings

    @GET
    @build_request
    def play_by_play_v2(self, play_by_play_v2=PlayByPlayV2):
        return play_by_play_v2

    @GET
    @build_request
    def player_awards(self, player_awards=PlayerAwards):
        return player_awards

    @GET
    @build_request
    def player_career_stats(self, player_career_stats=PlayerCareerStats):
        return player_career_stats

    @GET
    @build_request
    def player_compare(self, player_compare=PlayerCompare):
        return player_compare

    @GET
    @build_request
    def player_dashboard_by_clutch(self, player_dashboard_by_clutch=PlayerDashboardByClutch):
        return player_dashboard_by_clutch

    @GET
    @build_request
    def player_dashboard_by_game_splits(self, player_dashboard_by_game_splits=PlayerDashboardByGameSplits):
        return player_dashboard_by_game_splits

    @GET
    @build_request
    def player_dashboard_by_general_splits(self, player_dashboard_by_general_splits=PlayerDashboardByGeneralSplits):
        return player_dashboard_by_general_splits

    @GET
    @build_request
    def player_dashboard_by_last_n_games(self, player_dashboard_by_last_n_games=PlayerDashboardByLastNGames):
        return player_dashboard_by_last_n_games

    @GET
    @build_request
    def player_dashboard_by_opponent(self, player_dashboard_by_opponent=PlayerDashboardByOpponent):
        return player_dashboard_by_opponent

    @GET
    @build_request
    def player_dashboard_by_shooting_splits(self, player_dashboard_by_shooting_splits=PlayerDashboardByShootingSplits):
        return player_dashboard_by_shooting_splits

    @GET
    @build_request
    def player_dashboard_by_team_performance(
            self, player_dashboard_by_team_performance=PlayerDashboardByTeamPerformance):
        return player_dashboard_by_team_performance

    @GET
    @build_request
    def player_dashboard_by_year_over_year(self, player_dashboard_by_year_over_year=PlayerDashboardByYearOverYear):
        return player_dashboard_by_year_over_year

    @GET
    @build_request
    def player_dash_pt_pass(self, player_dash_pt_pass=PlayerDashPtPass):
        return player_dash_pt_pass

    @GET
    @build_request
    def player_dash_pt_reb(self, player_dash_pt_reb=PlayerDashPtReb):
        return player_dash_pt_reb

    @GET
    @build_request
    def player_dash_pt_shot_defend(self, player_dash_pt_shot_defend=PlayerDashPtShotDefend):
        return player_dash_pt_shot_defend

    @GET
    @build_request
    def player_dash_pt_shots(self, player_dash_pt_shots=PlayerDashPtShots):
        return player_dash_pt_shots

    @GET
    @build_request
    def player_fantasy_profile(self, player_fantasy_profile=PlayerFantasyProfile):
        return player_fantasy_profile

    @GET
    @build_request
    def player_fantasy_profile_bar_graph(self, player_fantasy_profile_bar_graph=PlayerFantasyProfileBarGraph):
        return player_fantasy_profile_bar_graph

    @GET
    @build_request
    def player_game_log(self, player_game_log=PlayerGameLog):
        return player_game_log

    @GET
    @build_request
    def player_game_streak_finder(self, player_game_streak_finder=PlayerGameStreakFinder):
        return player_game_streak_finder

    @GET
    @build_request
    def player_next_n_games(self, player_next_n_games=PlayerNextNGames):
        return player_next_n_games

    @GET
    @build_request
    def player_profile_v2(self, player_profile_v2=PlayerProfileV2):
        return player_profile_v2

    @GET
    @build_request
    def player_vs_player(self, player_vs_player=PlayerVsPlayer):
        return player_vs_player

    @GET
    @build_request
    def playoff_picture(self, playoff_picture=PlayoffPicture):
        return playoff_picture

    @GET
    @build_request
    def scoreboard(self, scoreboard=Scoreboard):
        return scoreboard

    @GET
    @build_request
    def scoreboard_v2(self, scoreboard_v2=ScoreboardV2):
        return scoreboard_v2

    @GET
    @build_request
    def shot_chart_detail(self, shot_chart_detail=ShotChartDetail):
        return shot_chart_detail

    @GET
    @build_request
    def shot_chart_lineup_detail(self, shot_chart_lineup_detail=ShotChartLineupDetail):
        return shot_chart_lineup_detail

    @GET
    @build_request
    def synergy_play_types(self, synergy_play_types=SynergyPlayTypes):
        return synergy_play_types

    @GET
    @build_request
    def team_and_players_vs_players(self, team_and_players_vs_players=TeamAndPlayersVsPlayers):
        return team_and_players_vs_players

    @GET
    @build_request
    def team_dashboard_by_clutch(self, team_dashboard_by_clutch=TeamDashboardByClutch):
        return team_dashboard_by_clutch

    @GET
    @build_request
    def team_dashboard_by_game_splits(self, team_dashboard_by_game_splits=TeamDashboardByGameSplits):
        return team_dashboard_by_game_splits

    @GET
    @build_request
    def team_dashboard_by_general_splits(self, team_dashboard_by_general_splits=TeamDashboardByGeneralSplits):
        return team_dashboard_by_general_splits

    @GET
    @build_request
    def team_dashboard_by_last_n_games(self, team_dashboard_by_last_n_games=TeamDashboardByLastNGames):
        return team_dashboard_by_last_n_games

    @GET
    @build_request
    def team_dashboard_by_opponent(self, team_dashboard_by_opponent=TeamDashboardByOpponent):
        return team_dashboard_by_opponent

    @GET
    @build_request
    def team_dashboard_by_shooting_splits(self, team_dashboard_by_shooting_splits=TeamDashboardByShootingSplits):
        return team_dashboard_by_shooting_splits

    @GET
    @build_request
    def team_dashboard_by_team_performance(self, team_dashboard_by_team_performance=TeamDashboardByTeamPerformance):
        return team_dashboard_by_team_performance

    @GET
    @build_request
    def team_dashboard_by_year_over_year(self, team_dashboard_by_year_over_year=TeamDashboardByYearOverYear):
        return team_dashboard_by_year_over_year

    @GET
    @build_request
    def team_dash_lineups(self, team_dash_lineups=TeamDashLineups):
        return team_dash_lineups

    @GET
    @build_request
    def team_dash_pt_pass(self, team_dash_pt_pass=TeamDashPtPass):
        return team_dash_pt_pass

    @GET
    @build_request
    def team_dash_pt_reb(self, team_dash_pt_reb=TeamDashPtReb):
        return team_dash_pt_reb

    @GET
    @build_request
    def team_dash_pt_shots(self, team_dash_pt_shots=TeamDashPtShots):
        return team_dash_pt_shots

    @GET
    @build_request
    def team_details(self, team_details=TeamDetails):
        return team_details

    @GET
    @build_request
    def team_game_log(self, team_game_log=TeamGameLog):
        return team_game_log

    @GET
    @build_request
    def team_game_streak_finder(self, team_game_streak_finder=TeamGameStreakFinder):
        return team_game_streak_finder

    @GET
    @build_request
    def team_historical_leaders(self, team_historical_leaders=TeamHistoricalLeaders):
        return team_historical_leaders

    @GET
    @build_request
    def team_info_common(self, team_info_common=TeamInfoCommon):
        return team_info_common

    @GET
    @build_request
    def team_player_dashboard(self, team_player_dashboard=TeamPlayerDashboard):
        return team_player_dashboard

    @GET
    @build_request
    def team_player_on_off_details(self, team_player_on_off_details=TeamPlayerOnOffDetails):
        return team_player_on_off_details

    @GET
    @build_request
    def team_player_on_off_summary(self, team_player_on_off_summary=TeamPlayerOnOffSummary):
        return team_player_on_off_summary

    @GET
    @build_request
    def team_vs_player(self, team_vs_player=TeamVsPlayer):
        return team_vs_player

    @GET
    @build_request
    def team_year_by_year_stats(self, team_year_by_year_stats=TeamYearByYearStats):
        return team_year_by_year_stats

    @GET
    @build_request
    def video_details(self, video_details=VideoDetails):
        return video_details

    @GET
    @build_request
    def video_events(self, video_events=VideoEvents):
        return video_events

    @GET
    @build_request
    def video_status(self, video_status=VideoStatus):
        return video_status
