---
layout: default
title: cstrike15_gcmessages.proto
parent: Protobufs
nav_exclude: true
---

# `cstrike15_gcmessages.proto`

**Imports:** `steammessages.proto`, `engine_gcmessages.proto`, `gcsdk_gcmessages.proto`

## Diagram

```mermaid
classDiagram
direction LR

  class GameServerPing {
    +int32 ping
    +uint32 ip
    +uint32 instances
  }

  class DataCenterPing {
    +fixed32 data_center_id
    +sint32 ping
  }

  class DetailedSearchStatistic {
    +uint32 game_type
    +uint32 search_time_avg
    +uint32 players_searching
  }

  class TournamentPlayer {
    +uint32 account_id
    +string player_nick
    +string player_name
    +uint32 player_dob
    +string player_flag
    +string player_location
    +string player_desc
  }

  class TournamentTeam {
    +int32 team_id
    +string team_tag
    +string team_flag
    +string team_name
    +List~TournamentPlayer~ players
  }

  class TournamentEvent {
    +int32 event_id
    +string event_tag
    +string event_name
    +uint32 event_time_start
    +uint32 event_time_end
    +int32 event_public
    +int32 event_stage_id
    +string event_stage_name
    +uint32 active_section_id
  }

  class GlobalStatistics {
    +uint32 players_online
    +uint32 servers_online
    +uint32 players_searching
    +uint32 servers_available
    +uint32 ongoing_matches
    +uint32 search_time_avg
    +List~DetailedSearchStatistic~ search_statistics
    +string main_post_url
    +uint32 required_appid_version
    +uint32 pricesheet_version
    +uint32 twitch_streams_version
    +uint32 active_tournament_eventid
    +uint32 active_survey_id
    +uint32 rtime32_cur
    +uint32 required_appid_version2
  }

  class OperationalStatisticDescription {
    +string name
    +uint32 idkey
  }

  class OperationalStatisticElement {
    +uint32 idkey
    +List~int32~ values
  }

  class OperationalStatisticsPacket {
    +int32 packetid
    +int32 mstimestamp
    +List~OperationalStatisticElement~ values
  }

  class OperationalVarValue {
    +string name
    +int32 ivalue
    +float fvalue
    +bytes svalue
  }

  class PlayerRankingInfo {
    +uint32 account_id
    +uint32 rank_id
    +uint32 wins
    +float rank_change
    +uint32 rank_type_id
    +uint32 tv_control
    +uint64 rank_window_stats
    +string leaderboard_name
    +uint32 rank_if_win
    +uint32 rank_if_lose
    +uint32 rank_if_tie
    +List~PlayerRankingInfo.PerMapRank~ per_map_rank
    +uint32 leaderboard_name_status
    +uint32 highest_rank
    +uint32 rank_expiry
  }

  class PerMapRank {
    +uint32 map_id
    +uint32 rank_id
    +uint32 wins
  }

  class PlayerCommendationInfo {
    +uint32 cmd_friendly
    +uint32 cmd_teaching
    +uint32 cmd_leader
  }

  class PlayerMedalsInfo {
    +List~uint32~ display_items_defidx
    +uint32 featured_display_item_defidx
  }

  class AccountActivity {
    +uint32 activity
    +uint32 mode
    +uint32 map
    +uint64 matchid
  }

  class TournamentMatchSetup {
    +int32 event_id
    +int32 team_id_ct
    +int32 team_id_t
    +int32 event_stage_id
  }

  class ServerHltvInfo {
    +uint32 tv_udp_port
    +uint64 tv_watch_key
    +uint32 tv_slots
    +uint32 tv_clients
    +uint32 tv_proxies
    +uint32 tv_time
    +uint32 game_type
    +string game_mapgroup
    +string game_map
    +uint64 tv_master_steamid
    +uint32 tv_local_slots
    +uint32 tv_local_clients
    +uint32 tv_local_proxies
    +uint32 tv_relay_slots
    +uint32 tv_relay_clients
    +uint32 tv_relay_proxies
    +uint32 tv_relay_address
    +uint32 tv_relay_port
    +uint64 tv_relay_steamid
    +uint32 flags
  }

  class IpAddressMask {
    +uint32 a
    +uint32 b
    +uint32 c
    +uint32 d
    +uint32 bits
    +uint32 token
  }

  class CMsgCsgoSteamUserStatChange {
    +int32 ecsgosteamuserstat
    +int32 delta
    +bool absolute
  }

  class XpProgressData {
    +uint32 xp_points
    +int32 xp_category
  }

  class MatchEndItemUpdates {
    +uint64 item_id
    +uint32 item_attr_defidx
    +uint32 item_attr_delta_value
  }

  class ScoreLeaderboardData {
    +uint64 quest_id
    +uint32 score
    +List~ScoreLeaderboardData.AccountEntries~ accountentries
    +List~ScoreLeaderboardData.Entry~ matchentries
    +string leaderboard_name
  }

  class Entry {
    +uint32 tag
    +uint32 val
  }

  class AccountEntries {
    +uint32 accountid
    +List~ScoreLeaderboardData.Entry~ entries
  }

  class PlayerQuestData {
    +uint32 quester_account_id
    +List~PlayerQuestData.QuestItemData~ quest_item_data
    +List~XpProgressData~ xp_progress_data
    +uint32 time_played
    +uint32 mm_game_mode
    +List~MatchEndItemUpdates~ item_updates
    +bool operation_points_eligible
    +List~CMsgCsgoSteamUserStatChange~ userstatchanges
  }

  class QuestItemData {
    +uint64 quest_id
    +int32 quest_normal_points_earned
    +int32 quest_bonus_points_earned
    +List~int32~ quest_normal_points_required
    +List~int32~ quest_reward_xp
    +int32 quest_period
    +QuestType quest_type
  }

  class DeepPlayerStatsEntry {
    +uint32 accountid
    +uint64 match_id
    +uint32 mm_game_mode
    +uint32 mapid
    +bool b_starting_ct
    +uint32 match_outcome
    +uint32 rounds_won
    +uint32 rounds_lost
    +uint32 stat_score
    +uint32 stat_deaths
    +uint32 stat_mvps
    +uint32 enemy_kills
    +uint32 enemy_headshots
    +uint32 enemy_2ks
    +uint32 enemy_3ks
    +uint32 enemy_4ks
    +uint32 total_damage
    +uint32 engagements_entry_count
    +uint32 engagements_entry_wins
    +uint32 engagements_1v1_count
    +uint32 engagements_1v1_wins
    +uint32 engagements_1v2_count
    +uint32 engagements_1v2_wins
    +uint32 utility_count
    +uint32 utility_success
    +uint32 flash_count
    +uint32 flash_success
    +List~uint32~ mates
  }

  class DeepPlayerMatchEvent {
    +uint32 accountid
    +uint64 match_id
    +uint32 event_id
    +uint32 event_type
    +bool b_playing_ct
    +int32 user_pos_x
    +int32 user_pos_y
    +int32 user_pos_z
    +uint32 user_defidx
    +int32 other_pos_x
    +int32 other_pos_y
    +int32 other_pos_z
    +uint32 other_defidx
    +int32 event_data
  }

  class CMsgGC_ServerQuestUpdateData {
    +List~PlayerQuestData~ player_quest_data
    +bytes binary_data
    +uint32 mm_game_mode
    +ScoreLeaderboardData missionlbsdata
    +uint32 flags
  }

  class CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm {
    +uint32 token
    +uint32 stamp
    +uint64 exchange
    +uint32 retry
  }

  class CMsgGCCStrike15_v2_GC2ServerReservationUpdate {
    +uint32 viewers_external_total
    +uint32 viewers_external_steam
  }

  class CMsgGCCStrike15_v2_MatchmakingStart {
    +List~uint32~ account_ids
    +uint32 game_type
    +string ticket_data
    +uint32 client_version
    +TournamentMatchSetup tournament_match
    +bool prime_only
    +uint32 tv_control
    +uint64 lobby_id
  }

  class CMsgGCCStrike15_v2_MatchmakingStop {
    +int32 abandon
  }

  class CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate_Note {
    +int32 type
    +int32 region_id
    +float region_r
    +float distance
  }

  class CMsgGCCStrike15_v2_MatchmakingClient2ServerPing {
    +List~GameServerPing~ gameserverpings
    +int32 offset_index
    +int32 final_batch
    +List~DataCenterPing~ data_center_pings
    +uint32 max_ping
    +fixed32 test_token
    +bytes search_key
    +List~CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate_Note~ notes
    +string debug_message
  }

  class CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate {
    +int32 matchmaking
    +List~uint32~ waiting_account_id_sessions
    +string error
    +List~uint32~ ongoingmatch_account_id_sessions
    +GlobalStatistics global_stats
    +List~uint32~ failping_account_id_sessions
    +List~uint32~ penalty_account_id_sessions
    +List~uint32~ failready_account_id_sessions
    +List~uint32~ vacbanned_account_id_sessions
    +IpAddressMask server_ipaddress_mask
    +List~CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate_Note~ notes
    +List~uint32~ penalty_account_id_sessions_green
    +List~uint32~ insufficientlevel_sessions
    +List~uint32~ vsncheck_account_id_sessions
    +List~uint32~ launcher_mismatch_sessions
    +List~uint32~ insecure_account_id_sessions
  }

  class CDataGCCStrike15_v2_TournamentMatchDraft {
    +int32 event_id
    +int32 event_stage_id
    +int32 team_id_0
    +int32 team_id_1
    +int32 maps_count
    +int32 maps_current
    +int32 team_id_start
    +int32 team_id_veto1
    +int32 team_id_pickn
    +List~CDataGCCStrike15_v2_TournamentMatchDraft.Entry~ drafts
    +List~int32~ vote_mapid_0
    +List~int32~ vote_mapid_1
    +List~int32~ vote_mapid_2
    +List~int32~ vote_mapid_3
    +List~int32~ vote_mapid_4
    +List~int32~ vote_mapid_5
    +List~int32~ vote_starting_side
    +int32 vote_phase
    +float vote_phase_start
    +float vote_phase_length
  }

  class Entry {
    +int32 mapid
    +int32 team_id_ct
  }

  class CPreMatchInfoData {
    +int32 predictions_pct
    +CDataGCCStrike15_v2_TournamentMatchDraft draft
    +List~CPreMatchInfoData.TeamStats~ stats
    +List~int32~ wins
  }

  class TeamStats {
    +int32 match_info_idxtxt
    +string match_info_txt
    +List~string~ match_info_teams
  }

  class CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve {
    +List~uint32~ account_ids
    +uint32 game_type
    +uint64 match_id
    +uint32 server_version
    +uint32 flags
    +List~PlayerRankingInfo~ rankings
    +uint64 encryption_key
    +uint64 encryption_key_pub
    +List~uint32~ party_ids
    +List~IpAddressMask~ whitelist
    +uint64 tv_master_steamid
    +TournamentEvent tournament_event
    +List~TournamentTeam~ tournament_teams
    +List~uint32~ tournament_casters_account_ids
    +uint64 tv_relay_steamid
    +CPreMatchInfoData pre_match_data
    +uint32 tv_control
    +List~OperationalVarValue~ op_var_values
    +uint32 socache_control
    +List~int32~ teammate_colors
    +uint32 match_id_additional
  }

  class CMsgGCCStrike15_v2_MatchmakingServerReservationResponse {
    +uint64 reservationid
    +CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve reservation
    +string map
    +uint64 gc_reservation_sent
    +uint32 server_version
    +ServerHltvInfo tv_info
    +List~uint32~ reward_player_accounts
    +List~uint32~ idle_player_accounts
    +uint32 reward_item_attr_def_idx
    +uint32 reward_item_attr_value
    +uint32 reward_item_attr_reward_idx
    +uint32 reward_drop_list
    +string tournament_tag
    +uint32 legacy_steamdatagram_port
    +uint32 steamdatagram_routing
    +fixed32 test_token
    +uint32 flags
    +uint32 system_load
    +uint32 cpus_online
  }

  class CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve {
    +uint64 serverid
    +uint32 direct_udp_ip
    +uint32 direct_udp_port
    +uint64 reservationid
    +CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve reservation
    +string map
    +string server_address
    +DataCenterPing gs_ping
    +uint32 gs_location_id
  }

  class CMsgGCCStrike15_v2_MatchmakingServerRoundStats {
    +uint64 reservationid
    +CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve reservation
    +string map
    +int32 round
    +List~int32~ kills
    +List~int32~ assists
    +List~int32~ deaths
    +List~int32~ scores
    +List~int32~ pings
    +int32 round_result
    +int32 match_result
    +List~int32~ team_scores
    +CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm confirm
    +int32 reservation_stage
    +int32 match_duration
    +List~int32~ enemy_kills
    +List~int32~ enemy_headshots
    +List~int32~ enemy_3ks
    +List~int32~ enemy_4ks
    +List~int32~ enemy_5ks
    +List~int32~ mvps
    +uint32 spectators_count
    +uint32 spectators_count_tv
    +uint32 spectators_count_lnk
    +List~int32~ enemy_kills_agg
    +CMsgGCCStrike15_v2_MatchmakingServerRoundStats.DropInfo drop_info
    +bool b_switched_teams
    +List~int32~ enemy_2ks
    +List~int32~ player_spawned
    +List~int32~ team_spawn_count
    +uint32 max_rounds
    +int32 map_id
  }

  class DropInfo {
    +uint32 account_mvp
  }

  class CMsgGCCStrike15_v2_MatchmakingClient2GCHello {
  }

  class CMsgGCCStrike15_v2_MatchmakingGC2ClientHello {
    +uint32 account_id
    +CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve ongoingmatch
    +GlobalStatistics global_stats
    +uint32 penalty_seconds
    +uint32 penalty_reason
    +int32 vac_banned
    +PlayerRankingInfo ranking
    +PlayerCommendationInfo commendation
    +PlayerMedalsInfo medals
    +TournamentEvent my_current_event
    +List~TournamentTeam~ my_current_event_teams
    +TournamentTeam my_current_team
    +List~TournamentEvent~ my_current_event_stages
    +uint32 survey_vote
    +AccountActivity activity
    +int32 player_level
    +int32 player_cur_xp
    +int32 player_xp_bonus_flags
    +List~PlayerRankingInfo~ rankings
    +uint64 owcaseid
  }

  class CMsgGCCStrike15_v2_AccountPrivacySettings {
    +List~CMsgGCCStrike15_v2_AccountPrivacySettings.Setting~ settings
  }

  class Setting {
    +uint32 setting_type
    +uint32 setting_value
  }

  class CMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon {
    +uint32 account_id
    +CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve abandoned_match
    +uint32 penalty_seconds
    +uint32 penalty_reason
  }

  class CMsgGCCStrike15_v2_ClientGCRankUpdate {
    +List~PlayerRankingInfo~ rankings
  }

  class CMsgGCCStrike15_v2_MatchmakingOperator2GCBlogUpdate {
    +string main_post_url
  }

  class CMsgGCCStrike15_v2_ServerNotificationForUserPenalty {
    +uint32 account_id
    +uint32 reason
    +uint32 seconds
    +bool communication_cooldown
  }

  class CMsgGCCStrike15_v2_ClientReportPlayer {
    +uint32 account_id
    +uint32 rpt_aimbot
    +uint32 rpt_wallhack
    +uint32 rpt_speedhack
    +uint32 rpt_teamharm
    +uint32 rpt_textabuse
    +uint32 rpt_voiceabuse
    +uint64 match_id
    +bool report_from_demo
  }

  class CMsgGCCStrike15_v2_ClientCommendPlayer {
    +uint32 account_id
    +uint64 match_id
    +PlayerCommendationInfo commendation
    +uint32 tokens
  }

  class CMsgGCCStrike15_v2_ClientReportServer {
    +uint32 rpt_poorperf
    +uint32 rpt_abusivemodels
    +uint32 rpt_badmotd
    +uint32 rpt_listingabuse
    +uint32 rpt_inventoryabuse
    +uint64 match_id
  }

  class CMsgGCCStrike15_v2_ClientReportResponse {
    +uint64 confirmation_id
    +uint32 account_id
    +uint32 server_ip
    +uint32 response_type
    +uint32 response_result
    +uint32 tokens
  }

  class CMsgGCCStrike15_v2_ClientRequestWatchInfoFriends {
    +uint32 request_id
    +List~uint32~ account_ids
    +uint64 serverid
    +uint64 matchid
    +uint32 client_launcher
    +List~DataCenterPing~ data_center_pings
  }

  class WatchableMatchInfo {
    +uint32 server_ip
    +uint32 tv_port
    +uint32 tv_spectators
    +uint32 tv_time
    +bytes tv_watch_password
    +uint64 cl_decryptdata_key
    +uint64 cl_decryptdata_key_pub
    +uint32 game_type
    +string game_mapgroup
    +string game_map
    +uint64 server_id
    +uint64 match_id
    +uint64 reservation_id
  }

  class CMsgGCCStrike15_v2_ClientRequestJoinFriendData {
    +uint32 version
    +uint32 account_id
    +uint32 join_token
    +uint32 join_ipp
    +CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve res
    +string errormsg
    +bool is_local_server
  }

  class CMsgGCCStrike15_v2_ClientRequestJoinServerData {
    +uint32 version
    +uint32 account_id
    +uint64 serverid
    +uint32 server_ip
    +uint32 server_port
    +CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve res
    +string errormsg
  }

  class CMsgGCCstrike15_v2_ClientRedeemMissionReward {
    +uint32 campaign_id
    +uint32 redeem_id
    +uint32 redeemable_balance
    +uint32 expected_cost
    +int32 bid_control
  }

  class CMsgGCCstrike15_v2_ClientRedeemFreeReward {
    +uint32 generation_time
    +uint32 redeemable_balance
    +List~uint64~ items
  }

  class CMsgGCCstrike15_v2_GC2ServerNotifyXPRewarded {
    +List~XpProgressData~ xp_progress_data
    +uint32 account_id
    +uint32 current_xp
    +uint32 current_level
    +uint32 upgraded_defidx
    +uint32 operation_points_awarded
    +uint32 free_rewards
    +uint32 xp_trail_remaining
    +int32 xp_trail_xp_needed
    +uint32 xp_trail_level
  }

  class CMsgGCCStrike15_v2_ClientNetworkConfig {
    +bytes data
  }

  class CMsgGCCStrike15_ClientDeepStats {
    +uint32 account_id
    +CMsgGCCStrike15_ClientDeepStats.DeepStatsRange range
    +List~CMsgGCCStrike15_ClientDeepStats.DeepStatsMatch~ matches
  }

  class DeepStatsRange {
    +uint32 begin
    +uint32 end
    +bool frozen
  }

  class DeepStatsMatch {
    +DeepPlayerStatsEntry player
    +List~DeepPlayerMatchEvent~ events
  }

  class CMsgGCCStrike15_v2_WatchInfoUsers {
    +uint32 request_id
    +List~uint32~ account_ids
    +List~WatchableMatchInfo~ watchable_match_infos
    +uint32 extended_timeout
  }

  class CMsgGCCStrike15_v2_ClientRequestPlayersProfile {
    +uint32 request_id__deprecated
    +List~uint32~ account_ids__deprecated
    +uint32 account_id
    +uint32 request_level
  }

  class CMsgGCCStrike15_v2_PlayersProfile {
    +uint32 request_id
    +List~CMsgGCCStrike15_v2_MatchmakingGC2ClientHello~ account_profiles
  }

  class CMsgGCCStrike15_v2_PremierSeasonSummary {
    +uint32 account_id
    +uint32 season_id
    +List~CMsgGCCStrike15_v2_PremierSeasonSummary.DataPerWeek~ data_per_week
    +List~CMsgGCCStrike15_v2_PremierSeasonSummary.DataPerMap~ data_per_map
  }

  class DataPerWeek {
    +uint64 week_id
    +uint32 rank_id
    +uint32 matches_played
  }

  class DataPerMap {
    +uint32 map_id
    +uint32 wins
    +uint32 ties
    +uint32 losses
    +uint32 rounds
    +uint32 kills
    +uint32 headshots
    +uint32 assists
    +uint32 deaths
    +uint32 mvps
    +uint32 rounds_3k
    +uint32 rounds_4k
    +uint32 rounds_5k
  }

  class CMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate {
    +uint64 caseid
    +uint32 suspectid
    +uint32 fractionid
    +uint32 rpt_aimbot
    +uint32 rpt_wallhack
    +uint32 rpt_speedhack
    +uint32 rpt_teamharm
    +uint32 reason
  }

  class CMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment {
    +uint64 caseid
    +string caseurl
    +uint32 verdict
    +uint32 timestamp
    +uint32 throttleseconds
    +uint32 suspectid
    +uint32 fractionid
    +uint32 numrounds
    +uint32 fractionrounds
    +int32 streakconvictions
    +uint32 reason
  }

  class CMsgGCCStrike15_v2_PlayerOverwatchCaseStatus {
    +uint64 caseid
    +uint32 statusid
  }

  class CClientHeaderOverwatchEvidence {
    +uint32 accountid
    +uint64 caseid
  }

  class CMsgGCCStrike15_v2_GC2ClientTextMsg {
    +uint32 id
    +uint32 type
    +bytes payload
  }

  class CMsgGCCStrike15_v2_Client2GCTextMsg {
    +uint32 id
    +List~bytes~ args
  }

  class CMsgGCCStrike15_v2_MatchEndRunRewardDrops {
    +CMsgGCCStrike15_v2_MatchmakingServerReservationResponse serverinfo
    +CMsgGC_ServerQuestUpdateData match_end_quest_data
  }

  class CEconItemPreviewDataBlock {
    +uint32 accountid
    +uint64 itemid
    +uint32 defindex
    +uint32 paintindex
    +uint32 rarity
    +uint32 quality
    +uint32 paintwear
    +uint32 paintseed
    +uint32 killeaterscoretype
    +uint32 killeatervalue
    +string customname
    +List~CEconItemPreviewDataBlock.Sticker~ stickers
    +uint32 inventory
    +uint32 origin
    +uint32 questid
    +uint32 dropreason
    +uint32 musicindex
    +int32 entindex
    +uint32 petindex
    +List~CEconItemPreviewDataBlock.Sticker~ keychains
    +uint32 style
    +List~CEconItemPreviewDataBlock.Sticker~ variations
    +uint32 upgrade_level
  }

  class Sticker {
    +uint32 slot
    +uint32 sticker_id
    +float wear
    +float scale
    +float rotation
    +uint32 tint_id
    +float offset_x
    +float offset_y
    +float offset_z
    +uint32 pattern
    +uint32 highlight_reel
    +uint32 wrapped_sticker
  }

  class CMsgGCCStrike15_v2_MatchEndRewardDropsNotification {
    +CEconItemPreviewDataBlock iteminfo
  }

  class CMsgItemAcknowledged {
    +CEconItemPreviewDataBlock iteminfo
  }

  class CMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest {
    +uint64 param_s
    +uint64 param_a
    +uint64 param_d
    +uint64 param_m
  }

  class CMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse {
    +CEconItemPreviewDataBlock iteminfo
  }

  class CMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames {
  }

  class CMsgGCCStrike15_v2_MatchListRequestLiveGameForUser {
    +uint32 accountid
  }

  class CMsgGCCStrike15_v2_MatchListRequestRecentUserGames {
    +uint32 accountid
  }

  class CMsgGCCStrike15_v2_MatchListRequestTournamentGames {
    +int32 eventid
  }

  class CMsgGCCStrike15_v2_MatchListRequestFullGameInfo {
    +uint64 matchid
    +uint64 outcomeid
    +uint32 token
  }

  class CDataGCCStrike15_v2_MatchInfo {
    +uint64 matchid
    +uint32 matchtime
    +WatchableMatchInfo watchablematchinfo
    +CMsgGCCStrike15_v2_MatchmakingServerRoundStats roundstats_legacy
    +List~CMsgGCCStrike15_v2_MatchmakingServerRoundStats~ roundstatsall
  }

  class CDataGCCStrike15_v2_TournamentGroupTeam {
    +int32 team_id
    +int32 score
    +bool correctpick
  }

  class CDataGCCStrike15_v2_TournamentGroup {
    +uint32 groupid
    +string name
    +string desc
    +uint32 picks__deprecated
    +List~CDataGCCStrike15_v2_TournamentGroupTeam~ teams
    +List~int32~ stage_ids
    +uint32 picklockuntiltime
    +uint32 pickableteams
    +uint32 points_per_pick
    +List~CDataGCCStrike15_v2_TournamentGroup.Picks~ picks
  }

  class Picks {
    +List~int32~ pickids
  }

  class CDataGCCStrike15_v2_TournamentSection {
    +uint32 sectionid
    +string name
    +string desc
    +List~CDataGCCStrike15_v2_TournamentGroup~ groups
  }

  class CDataGCCStrike15_v2_TournamentInfo {
    +List~CDataGCCStrike15_v2_TournamentSection~ sections
    +TournamentEvent tournament_event
    +List~TournamentTeam~ tournament_teams
  }

  class CMsgGCCStrike15_v2_MatchList {
    +uint32 msgrequestid
    +uint32 accountid
    +uint32 servertime
    +List~CDataGCCStrike15_v2_MatchInfo~ matches
    +List~TournamentTeam~ streams
    +CDataGCCStrike15_v2_TournamentInfo tournamentinfo
  }

  class CMsgGCCStrike15_v2_MatchListTournamentOperatorMgmt {
    +int32 eventid
    +List~CDataGCCStrike15_v2_MatchInfo~ matches
    +uint32 accountid
  }

  class CMsgGCCStrike15_v2_Predictions {
    +uint32 event_id
    +List~CMsgGCCStrike15_v2_Predictions.GroupMatchTeamPick~ group_match_team_picks
  }

  class GroupMatchTeamPick {
    +int32 sectionid
    +int32 groupid
    +int32 index
    +int32 teamid
    +uint64 itemid
  }

  class CMsgGCCStrike15_v2_Fantasy {
    +uint32 event_id
    +List~CMsgGCCStrike15_v2_Fantasy.FantasyTeam~ teams
  }

  class FantasySlot {
    +int32 type
    +int32 pick
    +uint64 itemid
  }

  class FantasyTeam {
    +int32 sectionid
    +List~CMsgGCCStrike15_v2_Fantasy.FantasySlot~ slots
  }

  class CAttribute_String {
    +string value
  }

  class CMsgLegacySource1ClientWelcome {
    +uint32 version
    +bytes game_data
    +List~CMsgSOCacheSubscribed~ outofdate_subscribed_caches
    +List~CMsgSOCacheSubscriptionCheck~ uptodate_subscribed_caches
    +CMsgLegacySource1ClientWelcome.Location location
    +bytes game_data2
    +uint32 rtime32_gc_welcome_timestamp
    +uint32 currency
    +uint32 balance
    +string balance_url
    +string txn_country_code
  }

  class Location {
    +float latitude
    +float longitude
    +string country
  }

  class CMsgCStrike15Welcome {
    +uint32 store_item_hash
    +uint32 timeplayedconsecutively
    +uint32 time_first_played
    +uint32 last_time_played
    +uint32 last_ip_address
    +uint64 gscookieid
    +uint64 uniqueid
  }

  class CMsgGCCStrike15_v2_ClientVarValueNotificationInfo {
    +string value_name
    +int32 value_int
    +uint32 server_addr
    +uint32 server_port
    +List~string~ choked_blocks
  }

  class CMsgGCCStrike15_v2_ServerVarValueNotificationInfo {
    +uint32 accountid
    +List~uint32~ viewangles
    +uint32 type
    +List~uint32~ userdata
  }

  class CMsgGCCStrike15_v2_GiftsLeaderboardRequest {
  }

  class CMsgGCCStrike15_v2_GiftsLeaderboardResponse {
    +uint32 servertime
    +uint32 time_period_seconds
    +uint32 total_gifts_given
    +uint32 total_givers
    +List~CMsgGCCStrike15_v2_GiftsLeaderboardResponse.GiftLeaderboardEntry~ entries
  }

  class GiftLeaderboardEntry {
    +uint32 accountid
    +uint32 gifts
  }

  class CMsgGCCStrike15_v2_ClientSubmitSurveyVote {
    +uint32 survey_id
    +uint32 vote
  }

  class CMsgGCCStrike15_v2_Server2GCClientValidate {
    +uint32 accountid
  }

  class CMsgGCCStrike15_v2_GC2ClientTournamentInfo {
    +uint32 eventid
    +uint32 stageid
    +uint32 game_type
    +List~uint32~ teamids
  }

  class CSOEconCoupon {
    +uint32 entryid
    +uint32 defidx
    +fixed32 expiration_date
  }

  class CSOAccountItemPersonalStore {
    +uint32 generation_time
    +uint32 redeemable_balance
    +List~uint64~ items
  }

  class CSOAccountXpShop {
    +uint32 generation_time
    +uint32 redeemable_balance
    +List~uint32~ xp_tracks
  }

  class CSOAccountXpShopBids {
    +uint32 campaign_id
    +uint32 redeem_id
    +uint32 expected_cost
    +uint32 generation_time
  }

  class CSOVolatileItemOffer {
    +uint32 defidx
    +List~uint64~ faux_itemid
    +List~uint32~ generation_time
  }

  class CSOVolatileItemClaimedRewards {
    +uint32 defidx
    +List~uint32~ reward
    +List~uint32~ generation_time
  }

  class CSOAccountKeychainRemoveToolCharges {
    +uint32 charges
  }

  class CSOQuestProgress {
    +uint32 questid
    +uint32 points_remaining
    +uint32 bonus_points
  }

  class CSOAccountSeasonalOperation {
    +uint32 season_value
    +uint32 tier_unlocked
    +uint32 premium_tiers
    +uint32 mission_id
    +uint32 missions_completed
    +uint32 redeemable_balance
    +uint32 season_pass_time
  }

  class CSOAccountRecurringSubscription {
    +uint32 time_next_cycle
    +uint32 time_initiated
  }

  class CSOGameAccountSteamChina {
    +uint32 time_last_update
    +uint32 time_comms_ban
    +uint32 time_play_ban
  }

  class CSOPersonaDataPublic {
    +int32 player_level
    +PlayerCommendationInfo commendation
    +bool elevated_state
    +uint32 xp_trail_timestamp_refresh
    +uint32 xp_trail_level
  }

  class CSOAccountRecurringMission {
    +uint32 account_id
    +uint32 mission_id
    +uint32 period
    +uint32 progress
  }

  class CMsgGCCStrike15_v2_GC2ClientNotifyXPShop {
    +CSOAccountXpShop prematch
    +CSOAccountXpShop postmatch
    +uint32 current_xp
    +uint32 current_level
  }

  class CMsgGCCStrike15_v2_Client2GcAckXPShopTracks {
  }

  class CMsgGCCStrike15_v2_MatchmakingGC2ClientSearchStats {
    +uint32 gs_location_id
    +uint32 data_center_id
    +uint32 num_locked_in
    +uint32 num_found_nearby
    +uint32 note_level
  }

  class CMsgGC_GlobalGame_Subscribe {
    +uint64 ticket
  }

  class CMsgGC_GlobalGame_Unsubscribe {
    +int32 timeleft
  }

  class CMsgGC_GlobalGame_Play {
    +uint64 ticket
    +uint32 gametimems
    +uint32 msperpoint
  }

  class CMsgGCCStrike15_v2_AcknowledgePenalty {
    +int32 acknowledged
  }

  class CMsgGCCStrike15_v2_Client2GCRequestPrestigeCoin {
    +uint32 defindex
    +uint64 upgradeid
    +uint32 hours
    +uint32 prestigetime
  }

  class CMsgGCCStrike15_v2_Client2GCStreamUnlock {
    +uint64 ticket
    +int32 os
  }

  class CMsgGCCStrike15_v2_ClientToGCRequestElevate {
    +uint32 stage
  }

  class CMsgGCCStrike15_v2_ClientToGCChat {
    +uint64 match_id
    +string text
  }

  class CMsgGCCStrike15_v2_GCToClientChat {
    +uint32 account_id
    +string text
  }

  class CMsgGCCStrike15_v2_ClientAuthKeyCode {
    +uint32 eventid
    +string code
  }

  class CMsgGCCStrike15_GotvSyncPacket {
    +CEngineGotvSyncPacket data
  }

  class PlayerDecalDigitalSignature {
    +bytes signature
    +uint32 accountid
    +uint32 rtime
    +List~float~ endpos
    +List~float~ startpos
    +List~float~ left
    +uint32 tx_defidx
    +int32 entindex
    +uint32 hitbox
    +float creationtime
    +uint32 equipslot
    +uint32 trace_id
    +List~float~ normal
    +uint32 tint_id
  }

  class CMsgGCCStrike15_v2_ClientPlayerDecalSign {
    +PlayerDecalDigitalSignature data
    +uint64 itemid
  }

  class CMsgGCCStrike15_v2_BetaEnrollment {
    +uint32 eresult
  }

  class CMsgGCCStrike15_v2_ClientLogonFatalError {
    +uint32 errorcode
    +string message
    +string country
  }

  class CMsgGCCStrike15_v2_ClientPollState {
    +uint32 pollid
    +List~string~ names
    +List~int32~ values
  }

  class CMsgGCCStrike15_v2_Party_Register {
    +uint32 id
    +uint32 ver
    +uint32 apr
    +uint32 ark
    +uint32 nby
    +uint32 grp
    +uint32 slots
    +uint32 launcher
    +uint32 game_type
  }

  class CMsgGCCStrike15_v2_Party_Search {
    +uint32 ver
    +uint32 apr
    +uint32 ark
    +List~uint32~ grps
    +uint32 launcher
    +uint32 game_type
  }

  class CMsgGCCStrike15_v2_Party_SearchResults {
    +List~CMsgGCCStrike15_v2_Party_SearchResults.Entry~ entries
  }

  class Entry {
    +uint32 id
    +uint32 grp
    +uint32 game_type
    +uint32 apr
    +uint32 ark
    +uint32 loc
    +uint32 accountid
  }

  class CMsgGCCStrike15_v2_Party_Invite {
    +uint32 accountid
    +uint32 lobbyid
  }

  class CMsgGCCStrike15_v2_Account_RequestCoPlays {
    +List~CMsgGCCStrike15_v2_Account_RequestCoPlays.Player~ players
    +uint32 servertime
  }

  class Player {
    +uint32 accountid
    +uint32 rtcoplay
    +bool online
  }

  class CMsgGCCStrike15_v2_ClientToGCRequestTicket {
    +fixed64 authorized_steam_id
    +fixed32 authorized_public_ip
    +fixed64 gameserver_steam_id
    +string gameserver_sdr_routing
  }

  class CMsgGCToClientSteamDatagramTicket {
    +bytes serialized_ticket
  }

  class CMsgGCCStrike15_v2_ClientRequestOffers {
  }

  class CMsgGCCStrike15_v2_ClientRequestSouvenir {
    +uint64 itemid
    +uint64 matchid
    +int32 eventid
  }

  class CMsgGCCStrike15_v2_ClientAccountBalance {
    +uint64 amount
    +string url
  }

  class CMsgGCCStrike15_v2_ClientPartyJoinRelay {
    +uint32 accountid
    +uint64 lobbyid
  }

  class CMsgGCCStrike15_v2_ClientPartyWarning {
    +List~CMsgGCCStrike15_v2_ClientPartyWarning.Entry~ entries
  }

  class Entry {
    +uint32 accountid
    +uint32 warntype
  }

  class CMsgGCCStrike15_v2_SetEventFavorite {
    +uint64 eventid
    +bool is_favorite
  }

  class CMsgGCCStrike15_v2_GetEventFavorites_Request {
    +bool all_events
  }

  class CMsgGCCStrike15_v2_GetEventFavorites_Response {
    +bool all_events
    +string json_favorites
    +string json_featured
  }

  class CMsgGCCStrike15_v2_ClientPerfReport {
    +List~CMsgGCCStrike15_v2_ClientPerfReport.Entry~ entries
  }

  class Entry {
    +uint32 perfcounter
    +uint32 length
    +bytes reference
    +bytes actual
    +uint32 sourceid
    +uint32 status
  }

  class CVDiagnostic {
    +uint32 id
    +uint32 extended
    +uint64 value
    +string string_value
  }

  class CMsgGCCStrike15_v2_GC2ClientRefuseSecureMode {
    +string file_report
    +bool offer_insecure_mode
    +bool offer_secure_mode
    +bool show_unsigned_ui
    +bool kick_user
    +bool show_trusted_ui
    +bool show_warning_not_trusted
    +bool show_warning_not_trusted_2
    +string files_prevented_trusted
  }

  class CMsgGCCStrike15_v2_GC2ClientRequestValidation {
    +bool full_report
    +string module
  }

  class CMsgGCCStrike15_v2_GC2ClientInitSystem {
    +bool load
    +string name
    +string outputname
    +bytes key_data
    +bytes sha_hash
    +int32 cookie
    +string manifest
    +bytes system_package
    +bool load_system
  }

  class CMsgGCCStrike15_v2_GC2ClientInitSystem_Response {
    +bool success
    +string diagnostic
    +bytes sha_hash
    +int32 response
    +int32 error_code1
    +int32 error_code2
    +int64 handle
    +EInitSystemResult einit_result
    +int32 aux_system1
    +int32 aux_system2
  }

  class CMsgGCCStrike15_v2_SetPlayerLeaderboardSafeName {
    +string leaderboard_safe_name
  }

  class CMsgRequestRecurringMissionSchedule {
  }

  class CMsgRecurringMissionSchema {
    +List~CMsgRecurringMissionSchema.MissionTemplateList~ missions
  }

  class MissionTemplateList {
    +uint32 period
    +List~bytes~ mission_templates
  }

  TournamentTeam --> TournamentPlayer : players[]
  GlobalStatistics --> DetailedSearchStatistic : search_statistics[]
  OperationalStatisticsPacket --> OperationalStatisticElement : values[]
  PlayerRankingInfo --> PerMapRank : per_map_rank[]
  ScoreLeaderboardData --> AccountEntries : accountentries[]
  ScoreLeaderboardData --> Entry : matchentries[]
  AccountEntries --> Entry : entries[]
  PlayerQuestData --> QuestItemData : quest_item_data[]
  PlayerQuestData --> XpProgressData : xp_progress_data[]
  PlayerQuestData --> MatchEndItemUpdates : item_updates[]
  PlayerQuestData --> CMsgCsgoSteamUserStatChange : userstatchanges[]
  QuestItemData --> QuestType : quest_type
  CMsgGC_ServerQuestUpdateData --> PlayerQuestData : player_quest_data[]
  CMsgGC_ServerQuestUpdateData --> ScoreLeaderboardData : missionlbsdata
  CMsgGCCStrike15_v2_MatchmakingStart --> TournamentMatchSetup : tournament_match
  CMsgGCCStrike15_v2_MatchmakingClient2ServerPing --> GameServerPing : gameserverpings[]
  CMsgGCCStrike15_v2_MatchmakingClient2ServerPing --> DataCenterPing : data_center_pings[]
  CMsgGCCStrike15_v2_MatchmakingClient2ServerPing --> CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate_Note : notes[]
  CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate --> GlobalStatistics : global_stats
  CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate --> IpAddressMask : server_ipaddress_mask
  CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate --> CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate_Note : notes[]
  CDataGCCStrike15_v2_TournamentMatchDraft --> Entry : drafts[]
  CPreMatchInfoData --> CDataGCCStrike15_v2_TournamentMatchDraft : draft
  CPreMatchInfoData --> TeamStats : stats[]
  CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve --> PlayerRankingInfo : rankings[]
  CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve --> IpAddressMask : whitelist[]
  CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve --> TournamentEvent : tournament_event
  CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve --> TournamentTeam : tournament_teams[]
  CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve --> CPreMatchInfoData : pre_match_data
  CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve --> OperationalVarValue : op_var_values[]
  CMsgGCCStrike15_v2_MatchmakingServerReservationResponse --> CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve : reservation
  CMsgGCCStrike15_v2_MatchmakingServerReservationResponse --> ServerHltvInfo : tv_info
  CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve --> CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve : reservation
  CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve --> DataCenterPing : gs_ping
  CMsgGCCStrike15_v2_MatchmakingServerRoundStats --> CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve : reservation
  CMsgGCCStrike15_v2_MatchmakingServerRoundStats --> CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm : confirm
  CMsgGCCStrike15_v2_MatchmakingServerRoundStats --> DropInfo : drop_info
  CMsgGCCStrike15_v2_MatchmakingGC2ClientHello --> CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve : ongoingmatch
  CMsgGCCStrike15_v2_MatchmakingGC2ClientHello --> GlobalStatistics : global_stats
  CMsgGCCStrike15_v2_MatchmakingGC2ClientHello --> PlayerRankingInfo : ranking
  CMsgGCCStrike15_v2_MatchmakingGC2ClientHello --> PlayerCommendationInfo : commendation
  CMsgGCCStrike15_v2_MatchmakingGC2ClientHello --> PlayerMedalsInfo : medals
  CMsgGCCStrike15_v2_MatchmakingGC2ClientHello --> TournamentEvent : my_current_event
  CMsgGCCStrike15_v2_MatchmakingGC2ClientHello --> TournamentTeam : my_current_event_teams[]
  CMsgGCCStrike15_v2_MatchmakingGC2ClientHello --> AccountActivity : activity
  CMsgGCCStrike15_v2_AccountPrivacySettings --> Setting : settings[]
  CMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon --> CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve : abandoned_match
  CMsgGCCStrike15_v2_ClientGCRankUpdate --> PlayerRankingInfo : rankings[]
  CMsgGCCStrike15_v2_ClientCommendPlayer --> PlayerCommendationInfo : commendation
  CMsgGCCStrike15_v2_ClientRequestWatchInfoFriends --> DataCenterPing : data_center_pings[]
  CMsgGCCStrike15_v2_ClientRequestJoinFriendData --> CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve : res
  CMsgGCCStrike15_v2_ClientRequestJoinServerData --> CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve : res
  CMsgGCCstrike15_v2_GC2ServerNotifyXPRewarded --> XpProgressData : xp_progress_data[]
  CMsgGCCStrike15_ClientDeepStats --> DeepStatsRange : range
  CMsgGCCStrike15_ClientDeepStats --> DeepStatsMatch : matches[]
  DeepStatsMatch --> DeepPlayerStatsEntry : player
  DeepStatsMatch --> DeepPlayerMatchEvent : events[]
  CMsgGCCStrike15_v2_WatchInfoUsers --> WatchableMatchInfo : watchable_match_infos[]
  CMsgGCCStrike15_v2_PlayersProfile --> CMsgGCCStrike15_v2_MatchmakingGC2ClientHello : account_profiles[]
  CMsgGCCStrike15_v2_PremierSeasonSummary --> DataPerWeek : data_per_week[]
  CMsgGCCStrike15_v2_PremierSeasonSummary --> DataPerMap : data_per_map[]
  CMsgGCCStrike15_v2_MatchEndRunRewardDrops --> CMsgGCCStrike15_v2_MatchmakingServerReservationResponse : serverinfo
  CMsgGCCStrike15_v2_MatchEndRunRewardDrops --> CMsgGC_ServerQuestUpdateData : match_end_quest_data
  CEconItemPreviewDataBlock --> Sticker : stickers[]
  CMsgGCCStrike15_v2_MatchEndRewardDropsNotification --> CEconItemPreviewDataBlock : iteminfo
  CMsgItemAcknowledged --> CEconItemPreviewDataBlock : iteminfo
  CMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse --> CEconItemPreviewDataBlock : iteminfo
  CDataGCCStrike15_v2_MatchInfo --> WatchableMatchInfo : watchablematchinfo
  CDataGCCStrike15_v2_MatchInfo --> CMsgGCCStrike15_v2_MatchmakingServerRoundStats : roundstats_legacy
  CDataGCCStrike15_v2_TournamentGroup --> CDataGCCStrike15_v2_TournamentGroupTeam : teams[]
  CDataGCCStrike15_v2_TournamentGroup --> Picks : picks[]
  CDataGCCStrike15_v2_TournamentSection --> CDataGCCStrike15_v2_TournamentGroup : groups[]
  CDataGCCStrike15_v2_TournamentInfo --> CDataGCCStrike15_v2_TournamentSection : sections[]
  CDataGCCStrike15_v2_TournamentInfo --> TournamentEvent : tournament_event
  CDataGCCStrike15_v2_TournamentInfo --> TournamentTeam : tournament_teams[]
  CMsgGCCStrike15_v2_MatchList --> CDataGCCStrike15_v2_MatchInfo : matches[]
  CMsgGCCStrike15_v2_MatchList --> TournamentTeam : streams[]
  CMsgGCCStrike15_v2_MatchList --> CDataGCCStrike15_v2_TournamentInfo : tournamentinfo
  CMsgGCCStrike15_v2_MatchListTournamentOperatorMgmt --> CDataGCCStrike15_v2_MatchInfo : matches[]
  CMsgGCCStrike15_v2_Predictions --> GroupMatchTeamPick : group_match_team_picks[]
  CMsgGCCStrike15_v2_Fantasy --> FantasyTeam : teams[]
  FantasyTeam --> FantasySlot : slots[]
  CMsgLegacySource1ClientWelcome --> Location : location
  CMsgGCCStrike15_v2_GiftsLeaderboardResponse --> GiftLeaderboardEntry : entries[]
  CSOPersonaDataPublic --> PlayerCommendationInfo : commendation
  CMsgGCCStrike15_v2_GC2ClientNotifyXPShop --> CSOAccountXpShop : prematch
  CMsgGCCStrike15_v2_ClientPlayerDecalSign --> PlayerDecalDigitalSignature : data
  CMsgGCCStrike15_v2_Party_SearchResults --> Entry : entries[]
  CMsgGCCStrike15_v2_Account_RequestCoPlays --> Player : players[]
  CMsgGCCStrike15_v2_ClientPartyWarning --> Entry : entries[]
  CMsgGCCStrike15_v2_ClientPerfReport --> Entry : entries[]
  CMsgGCCStrike15_v2_GC2ClientInitSystem_Response --> EInitSystemResult : einit_result
  CMsgRecurringMissionSchema --> MissionTemplateList : missions[]

  class ECsgoGCMsg{
    <<enumeration>>
    k_EMsgGCCStrike15_v2_Base
    k_EMsgGCCStrike15_v2_MatchmakingStart
    k_EMsgGCCStrike15_v2_MatchmakingStop
    k_EMsgGCCStrike15_v2_MatchmakingClient2ServerPing
    k_EMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate
    k_EMsgGCCStrike15_v2_MatchmakingServerReservationResponse
    k_EMsgGCCStrike15_v2_MatchmakingGC2ClientReserve
    k_EMsgGCCStrike15_v2_MatchmakingClient2GCHello
    k_EMsgGCCStrike15_v2_MatchmakingGC2ClientHello
    k_EMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon
    k_EMsgGCCStrike15_v2_MatchmakingOperator2GCBlogUpdate
    k_EMsgGCCStrike15_v2_ServerNotificationForUserPenalty
    k_EMsgGCCStrike15_v2_ClientReportPlayer
    k_EMsgGCCStrike15_v2_ClientReportServer
    k_EMsgGCCStrike15_v2_ClientCommendPlayer
    k_EMsgGCCStrike15_v2_ClientReportResponse
    k_EMsgGCCStrike15_v2_ClientCommendPlayerQuery
    k_EMsgGCCStrike15_v2_ClientCommendPlayerQueryResponse
    k_EMsgGCCStrike15_v2_WatchInfoUsers
    k_EMsgGCCStrike15_v2_ClientRequestPlayersProfile
    k_EMsgGCCStrike15_v2_PlayersProfile
    k_EMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate
    k_EMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment
    k_EMsgGCCStrike15_v2_PlayerOverwatchCaseStatus
    k_EMsgGCCStrike15_v2_GC2ClientTextMsg
    k_EMsgGCCStrike15_v2_Client2GCTextMsg
    k_EMsgGCCStrike15_v2_MatchEndRunRewardDrops
    k_EMsgGCCStrike15_v2_MatchEndRewardDropsNotification
    k_EMsgGCCStrike15_v2_ClientRequestWatchInfoFriends2
    k_EMsgGCCStrike15_v2_MatchList
    k_EMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames
    k_EMsgGCCStrike15_v2_MatchListRequestRecentUserGames
    k_EMsgGCCStrike15_v2_GC2ServerReservationUpdate
    k_EMsgGCCStrike15_v2_ClientVarValueNotificationInfo
    k_EMsgGCCStrike15_v2_MatchListRequestTournamentGames
    k_EMsgGCCStrike15_v2_MatchListRequestFullGameInfo
    k_EMsgGCCStrike15_v2_GiftsLeaderboardRequest
    k_EMsgGCCStrike15_v2_GiftsLeaderboardResponse
    k_EMsgGCCStrike15_v2_ServerVarValueNotificationInfo
    k_EMsgGCCStrike15_v2_ClientSubmitSurveyVote
    k_EMsgGCCStrike15_v2_Server2GCClientValidate
    k_EMsgGCCStrike15_v2_MatchListRequestLiveGameForUser
    k_EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest
    k_EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse
    k_EMsgGCCStrike15_v2_AccountPrivacySettings
    k_EMsgGCCStrike15_v2_SetMyActivityInfo
    k_EMsgGCCStrike15_v2_MatchListRequestTournamentPredictions
    k_EMsgGCCStrike15_v2_MatchListUploadTournamentPredictions
    k_EMsgGCCStrike15_v2_DraftSummary
    k_EMsgGCCStrike15_v2_ClientRequestJoinFriendData
    k_EMsgGCCStrike15_v2_ClientRequestJoinServerData
    k_EMsgGCCStrike15_v2_GC2ClientTournamentInfo
    k_EMsgGC_GlobalGame_Subscribe
    k_EMsgGC_GlobalGame_Unsubscribe
    k_EMsgGC_GlobalGame_Play
    k_EMsgGCCStrike15_v2_AcknowledgePenalty
    k_EMsgGCCStrike15_v2_Client2GCRequestPrestigeCoin
    k_EMsgGCCStrike15_v2_GC2ClientGlobalStats
    k_EMsgGCCStrike15_v2_Client2GCStreamUnlock
    k_EMsgGCCStrike15_v2_FantasyRequestClientData
    k_EMsgGCCStrike15_v2_FantasyUpdateClientData
    k_EMsgGCCStrike15_v2_GCToClientSteamdatagramTicket
    k_EMsgGCCStrike15_v2_ClientToGCRequestTicket
    k_EMsgGCCStrike15_v2_ClientToGCRequestElevate
    k_EMsgGCCStrike15_v2_GlobalChat
    k_EMsgGCCStrike15_v2_GlobalChat_Subscribe
    k_EMsgGCCStrike15_v2_GlobalChat_Unsubscribe
    k_EMsgGCCStrike15_v2_ClientAuthKeyCode
    k_EMsgGCCStrike15_v2_GotvSyncPacket
    k_EMsgGCCStrike15_v2_ClientPlayerDecalSign
    k_EMsgGCCStrike15_v2_ClientLogonFatalError
    k_EMsgGCCStrike15_v2_ClientPollState
    k_EMsgGCCStrike15_v2_Party_Register
    k_EMsgGCCStrike15_v2_Party_Unregister
    k_EMsgGCCStrike15_v2_Party_Search
    k_EMsgGCCStrike15_v2_Party_Invite
    k_EMsgGCCStrike15_v2_Account_RequestCoPlays
    k_EMsgGCCStrike15_v2_ClientGCRankUpdate
    k_EMsgGCCStrike15_v2_ClientRequestOffers
    k_EMsgGCCStrike15_v2_ClientAccountBalance
    k_EMsgGCCStrike15_v2_ClientPartyJoinRelay
    k_EMsgGCCStrike15_v2_ClientPartyWarning
    k_EMsgGCCStrike15_v2_SetEventFavorite
    k_EMsgGCCStrike15_v2_GetEventFavorites_Request
    k_EMsgGCCStrike15_v2_ClientPerfReport
    k_EMsgGCCStrike15_v2_GetEventFavorites_Response
    k_EMsgGCCStrike15_v2_ClientRequestSouvenir
    k_EMsgGCCStrike15_v2_GC2ClientRefuseSecureMode
    k_EMsgGCCStrike15_v2_GC2ClientRequestValidation
    k_EMsgGCCStrike15_v2_ClientRedeemMissionReward
    k_EMsgGCCStrike15_ClientDeepStats
    k_EMsgGCCStrike15_StartAgreementSessionInGame
    k_EMsgGCCStrike15_v2_GC2ClientInitSystem
    k_EMsgGCCStrike15_v2_GC2ClientInitSystem_Response
    k_EMsgGCCStrike15_v2_PrivateQueues
    k_EMsgGCCStrike15_v2_MatchListTournamentOperatorMgmt
    k_EMsgGCCStrike15_v2_BetaEnrollment
    k_EMsgGCCStrike15_v2_SetPlayerLeaderboardSafeName
    k_EMsgGCCStrike15_v2_ClientRedeemFreeReward
    k_EMsgGCCStrike15_v2_ClientNetworkConfig
    k_EMsgGCCStrike15_v2_GC2ClientNotifyXPShop
    k_EMsgGCCStrike15_v2_Client2GcAckXPShopTracks
    k_EMsgGCCStrike15_v2_MatchmakingGC2ClientSearchStats
    k_EMsgGCCStrike15_v2_PremierSeasonSummary
    k_EMsgGCCStrike15_v2_RequestRecurringMissionSchedule
    k_EMsgGCCStrike15_v2_RecurringMissionSchema
    k_EMsgGCCStrike15_v2_VolatileItemClaimReward
  }

  class ECsgoSteamUserStat{
    <<enumeration>>
    k_ECsgoSteamUserStat_XpEarnedGames
    k_ECsgoSteamUserStat_MatchWinsCompetitive
    k_ECsgoSteamUserStat_SurvivedDangerZone
  }

  class QuestType{
    <<enumeration>>
    k_EQuestType_Operation
    k_EQuestType_RecurringMission
  }

  class EClientReportingVersion{
    <<enumeration>>
    k_EClientReportingVersion_OldVersion
    k_EClientReportingVersion_BetaVersion
    k_EClientReportingVersion_SupportsTrustedMode
  }

  class EInitSystemResult{
    <<enumeration>>
    k_EInitSystemResult_Invalid
    k_EInitSystemResult_Success
    k_EInitSystemResult_None
    k_EInitSystemResult_NotFound
    k_EInitSystemResult_Existing
    k_EInitSystemResult_FailedOpen
    k_EInitSystemResult_Mismatch
    k_EInitSystemResult_FailedInit
    k_EInitSystemResult_Max
  }

```

## Enums

### `ECsgoGCMsg`

| Name | Value |
|------|-------|
| `k_EMsgGCCStrike15_v2_Base` | 9100 |
| `k_EMsgGCCStrike15_v2_MatchmakingStart` | 9101 |
| `k_EMsgGCCStrike15_v2_MatchmakingStop` | 9102 |
| `k_EMsgGCCStrike15_v2_MatchmakingClient2ServerPing` | 9103 |
| `k_EMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate` | 9104 |
| `k_EMsgGCCStrike15_v2_MatchmakingServerReservationResponse` | 9106 |
| `k_EMsgGCCStrike15_v2_MatchmakingGC2ClientReserve` | 9107 |
| `k_EMsgGCCStrike15_v2_MatchmakingClient2GCHello` | 9109 |
| `k_EMsgGCCStrike15_v2_MatchmakingGC2ClientHello` | 9110 |
| `k_EMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon` | 9112 |
| `k_EMsgGCCStrike15_v2_MatchmakingOperator2GCBlogUpdate` | 9117 |
| `k_EMsgGCCStrike15_v2_ServerNotificationForUserPenalty` | 9118 |
| `k_EMsgGCCStrike15_v2_ClientReportPlayer` | 9119 |
| `k_EMsgGCCStrike15_v2_ClientReportServer` | 9120 |
| `k_EMsgGCCStrike15_v2_ClientCommendPlayer` | 9121 |
| `k_EMsgGCCStrike15_v2_ClientReportResponse` | 9122 |
| `k_EMsgGCCStrike15_v2_ClientCommendPlayerQuery` | 9123 |
| `k_EMsgGCCStrike15_v2_ClientCommendPlayerQueryResponse` | 9124 |
| `k_EMsgGCCStrike15_v2_WatchInfoUsers` | 9126 |
| `k_EMsgGCCStrike15_v2_ClientRequestPlayersProfile` | 9127 |
| `k_EMsgGCCStrike15_v2_PlayersProfile` | 9128 |
| `k_EMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate` | 9131 |
| `k_EMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment` | 9132 |
| `k_EMsgGCCStrike15_v2_PlayerOverwatchCaseStatus` | 9133 |
| `k_EMsgGCCStrike15_v2_GC2ClientTextMsg` | 9134 |
| `k_EMsgGCCStrike15_v2_Client2GCTextMsg` | 9135 |
| `k_EMsgGCCStrike15_v2_MatchEndRunRewardDrops` | 9136 |
| `k_EMsgGCCStrike15_v2_MatchEndRewardDropsNotification` | 9137 |
| `k_EMsgGCCStrike15_v2_ClientRequestWatchInfoFriends2` | 9138 |
| `k_EMsgGCCStrike15_v2_MatchList` | 9139 |
| `k_EMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames` | 9140 |
| `k_EMsgGCCStrike15_v2_MatchListRequestRecentUserGames` | 9141 |
| `k_EMsgGCCStrike15_v2_GC2ServerReservationUpdate` | 9142 |
| `k_EMsgGCCStrike15_v2_ClientVarValueNotificationInfo` | 9144 |
| `k_EMsgGCCStrike15_v2_MatchListRequestTournamentGames` | 9146 |
| `k_EMsgGCCStrike15_v2_MatchListRequestFullGameInfo` | 9147 |
| `k_EMsgGCCStrike15_v2_GiftsLeaderboardRequest` | 9148 |
| `k_EMsgGCCStrike15_v2_GiftsLeaderboardResponse` | 9149 |
| `k_EMsgGCCStrike15_v2_ServerVarValueNotificationInfo` | 9150 |
| `k_EMsgGCCStrike15_v2_ClientSubmitSurveyVote` | 9152 |
| `k_EMsgGCCStrike15_v2_Server2GCClientValidate` | 9153 |
| `k_EMsgGCCStrike15_v2_MatchListRequestLiveGameForUser` | 9154 |
| `k_EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest` | 9156 |
| `k_EMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse` | 9157 |
| `k_EMsgGCCStrike15_v2_AccountPrivacySettings` | 9158 |
| `k_EMsgGCCStrike15_v2_SetMyActivityInfo` | 9159 |
| `k_EMsgGCCStrike15_v2_MatchListRequestTournamentPredictions` | 9160 |
| `k_EMsgGCCStrike15_v2_MatchListUploadTournamentPredictions` | 9161 |
| `k_EMsgGCCStrike15_v2_DraftSummary` | 9162 |
| `k_EMsgGCCStrike15_v2_ClientRequestJoinFriendData` | 9163 |
| `k_EMsgGCCStrike15_v2_ClientRequestJoinServerData` | 9164 |
| `k_EMsgGCCStrike15_v2_GC2ClientTournamentInfo` | 9167 |
| `k_EMsgGC_GlobalGame_Subscribe` | 9168 |
| `k_EMsgGC_GlobalGame_Unsubscribe` | 9169 |
| `k_EMsgGC_GlobalGame_Play` | 9170 |
| `k_EMsgGCCStrike15_v2_AcknowledgePenalty` | 9171 |
| `k_EMsgGCCStrike15_v2_Client2GCRequestPrestigeCoin` | 9172 |
| `k_EMsgGCCStrike15_v2_GC2ClientGlobalStats` | 9173 |
| `k_EMsgGCCStrike15_v2_Client2GCStreamUnlock` | 9174 |
| `k_EMsgGCCStrike15_v2_FantasyRequestClientData` | 9175 |
| `k_EMsgGCCStrike15_v2_FantasyUpdateClientData` | 9176 |
| `k_EMsgGCCStrike15_v2_GCToClientSteamdatagramTicket` | 9177 |
| `k_EMsgGCCStrike15_v2_ClientToGCRequestTicket` | 9178 |
| `k_EMsgGCCStrike15_v2_ClientToGCRequestElevate` | 9179 |
| `k_EMsgGCCStrike15_v2_GlobalChat` | 9180 |
| `k_EMsgGCCStrike15_v2_GlobalChat_Subscribe` | 9181 |
| `k_EMsgGCCStrike15_v2_GlobalChat_Unsubscribe` | 9182 |
| `k_EMsgGCCStrike15_v2_ClientAuthKeyCode` | 9183 |
| `k_EMsgGCCStrike15_v2_GotvSyncPacket` | 9184 |
| `k_EMsgGCCStrike15_v2_ClientPlayerDecalSign` | 9185 |
| `k_EMsgGCCStrike15_v2_ClientLogonFatalError` | 9187 |
| `k_EMsgGCCStrike15_v2_ClientPollState` | 9188 |
| `k_EMsgGCCStrike15_v2_Party_Register` | 9189 |
| `k_EMsgGCCStrike15_v2_Party_Unregister` | 9190 |
| `k_EMsgGCCStrike15_v2_Party_Search` | 9191 |
| `k_EMsgGCCStrike15_v2_Party_Invite` | 9192 |
| `k_EMsgGCCStrike15_v2_Account_RequestCoPlays` | 9193 |
| `k_EMsgGCCStrike15_v2_ClientGCRankUpdate` | 9194 |
| `k_EMsgGCCStrike15_v2_ClientRequestOffers` | 9195 |
| `k_EMsgGCCStrike15_v2_ClientAccountBalance` | 9196 |
| `k_EMsgGCCStrike15_v2_ClientPartyJoinRelay` | 9197 |
| `k_EMsgGCCStrike15_v2_ClientPartyWarning` | 9198 |
| `k_EMsgGCCStrike15_v2_SetEventFavorite` | 9200 |
| `k_EMsgGCCStrike15_v2_GetEventFavorites_Request` | 9201 |
| `k_EMsgGCCStrike15_v2_ClientPerfReport` | 9202 |
| `k_EMsgGCCStrike15_v2_GetEventFavorites_Response` | 9203 |
| `k_EMsgGCCStrike15_v2_ClientRequestSouvenir` | 9204 |
| `k_EMsgGCCStrike15_v2_GC2ClientRefuseSecureMode` | 9206 |
| `k_EMsgGCCStrike15_v2_GC2ClientRequestValidation` | 9207 |
| `k_EMsgGCCStrike15_v2_ClientRedeemMissionReward` | 9209 |
| `k_EMsgGCCStrike15_ClientDeepStats` | 9210 |
| `k_EMsgGCCStrike15_StartAgreementSessionInGame` | 9211 |
| `k_EMsgGCCStrike15_v2_GC2ClientInitSystem` | 9212 |
| `k_EMsgGCCStrike15_v2_GC2ClientInitSystem_Response` | 9213 |
| `k_EMsgGCCStrike15_v2_PrivateQueues` | 9214 |
| `k_EMsgGCCStrike15_v2_MatchListTournamentOperatorMgmt` | 9215 |
| `k_EMsgGCCStrike15_v2_BetaEnrollment` | 9217 |
| `k_EMsgGCCStrike15_v2_SetPlayerLeaderboardSafeName` | 9218 |
| `k_EMsgGCCStrike15_v2_ClientRedeemFreeReward` | 9219 |
| `k_EMsgGCCStrike15_v2_ClientNetworkConfig` | 9220 |
| `k_EMsgGCCStrike15_v2_GC2ClientNotifyXPShop` | 9221 |
| `k_EMsgGCCStrike15_v2_Client2GcAckXPShopTracks` | 9222 |
| `k_EMsgGCCStrike15_v2_MatchmakingGC2ClientSearchStats` | 9223 |
| `k_EMsgGCCStrike15_v2_PremierSeasonSummary` | 9224 |
| `k_EMsgGCCStrike15_v2_RequestRecurringMissionSchedule` | 9225 |
| `k_EMsgGCCStrike15_v2_RecurringMissionSchema` | 9226 |
| `k_EMsgGCCStrike15_v2_VolatileItemClaimReward` | 9227 |

### `ECsgoSteamUserStat`

| Name | Value |
|------|-------|
| `k_ECsgoSteamUserStat_XpEarnedGames` | 1 |
| `k_ECsgoSteamUserStat_MatchWinsCompetitive` | 2 |
| `k_ECsgoSteamUserStat_SurvivedDangerZone` | 3 |

### `QuestType`

| Name | Value |
|------|-------|
| `k_EQuestType_Operation` | 1 |
| `k_EQuestType_RecurringMission` | 2 |

### `EClientReportingVersion`

| Name | Value |
|------|-------|
| `k_EClientReportingVersion_OldVersion` | 0 |
| `k_EClientReportingVersion_BetaVersion` | 1 |
| `k_EClientReportingVersion_SupportsTrustedMode` | 2 |

### `EInitSystemResult`

| Name | Value |
|------|-------|
| `k_EInitSystemResult_Invalid` | 0 |
| `k_EInitSystemResult_Success` | 1 |
| `k_EInitSystemResult_None` | 2 |
| `k_EInitSystemResult_NotFound` | 3 |
| `k_EInitSystemResult_Existing` | 4 |
| `k_EInitSystemResult_FailedOpen` | 5 |
| `k_EInitSystemResult_Mismatch` | 6 |
| `k_EInitSystemResult_FailedInit` | 7 |
| `k_EInitSystemResult_Max` | 8 |

## Messages

### `GameServerPing`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ping` | 2 | int32 | optional |  |
| `ip` | 3 | uint32 | optional |  |
| `instances` | 5 | uint32 | optional |  |

### `DataCenterPing`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `data_center_id` | 1 | fixed32 | optional |  |
| `ping` | 2 | sint32 | optional |  |

### `DetailedSearchStatistic`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `game_type` | 1 | uint32 | optional |  |
| `search_time_avg` | 2 | uint32 | optional |  |
| `players_searching` | 4 | uint32 | optional |  |

### `TournamentPlayer`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `player_nick` | 2 | string | optional |  |
| `player_name` | 3 | string | optional |  |
| `player_dob` | 4 | uint32 | optional |  |
| `player_flag` | 5 | string | optional |  |
| `player_location` | 6 | string | optional |  |
| `player_desc` | 7 | string | optional |  |

### `TournamentTeam`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `team_id` | 1 | int32 | optional |  |
| `team_tag` | 2 | string | optional |  |
| `team_flag` | 3 | string | optional |  |
| `team_name` | 4 | string | optional |  |
| `players` | 5 | [TournamentPlayer](#tournamentplayer) | repeated |  |

### `TournamentEvent`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `event_id` | 1 | int32 | optional |  |
| `event_tag` | 2 | string | optional |  |
| `event_name` | 3 | string | optional |  |
| `event_time_start` | 4 | uint32 | optional |  |
| `event_time_end` | 5 | uint32 | optional |  |
| `event_public` | 6 | int32 | optional |  |
| `event_stage_id` | 7 | int32 | optional |  |
| `event_stage_name` | 8 | string | optional |  |
| `active_section_id` | 9 | uint32 | optional |  |

### `GlobalStatistics`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `players_online` | 1 | uint32 | optional |  |
| `servers_online` | 2 | uint32 | optional |  |
| `players_searching` | 3 | uint32 | optional |  |
| `servers_available` | 4 | uint32 | optional |  |
| `ongoing_matches` | 5 | uint32 | optional |  |
| `search_time_avg` | 6 | uint32 | optional |  |
| `search_statistics` | 7 | [DetailedSearchStatistic](#detailedsearchstatistic) | repeated |  |
| `main_post_url` | 8 | string | optional |  |
| `required_appid_version` | 9 | uint32 | optional |  |
| `pricesheet_version` | 10 | uint32 | optional |  |
| `twitch_streams_version` | 11 | uint32 | optional |  |
| `active_tournament_eventid` | 12 | uint32 | optional |  |
| `active_survey_id` | 13 | uint32 | optional |  |
| `rtime32_cur` | 14 | uint32 | optional |  |
| `required_appid_version2` | 16 | uint32 | optional |  |

### `OperationalStatisticDescription`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `name` | 1 | string | optional |  |
| `idkey` | 2 | uint32 | optional |  |

### `OperationalStatisticElement`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `idkey` | 1 | uint32 | optional |  |
| `values` | 2 | int32 | repeated |  |

### `OperationalStatisticsPacket`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `packetid` | 1 | int32 | optional |  |
| `mstimestamp` | 2 | int32 | optional |  |
| `values` | 3 | [OperationalStatisticElement](#operationalstatisticelement) | repeated |  |

### `OperationalVarValue`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `name` | 1 | string | optional |  |
| `ivalue` | 2 | int32 | optional |  |
| `fvalue` | 3 | float | optional |  |
| `svalue` | 4 | bytes | optional |  |

### `PlayerRankingInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `rank_id` | 2 | uint32 | optional |  |
| `wins` | 3 | uint32 | optional |  |
| `rank_change` | 4 | float | optional |  |
| `rank_type_id` | 6 | uint32 | optional |  |
| `tv_control` | 7 | uint32 | optional |  |
| `rank_window_stats` | 8 | uint64 | optional |  |
| `leaderboard_name` | 9 | string | optional |  |
| `rank_if_win` | 10 | uint32 | optional |  |
| `rank_if_lose` | 11 | uint32 | optional |  |
| `rank_if_tie` | 12 | uint32 | optional |  |
| `per_map_rank` | 13 | PlayerRankingInfo.PerMapRank | repeated |  |
| `leaderboard_name_status` | 14 | uint32 | optional |  |
| `highest_rank` | 15 | uint32 | optional |  |
| `rank_expiry` | 16 | uint32 | optional |  |

### `PlayerCommendationInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `cmd_friendly` | 1 | uint32 | optional |  |
| `cmd_teaching` | 2 | uint32 | optional |  |
| `cmd_leader` | 4 | uint32 | optional |  |

### `PlayerMedalsInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `display_items_defidx` | 7 | uint32 | repeated |  |
| `featured_display_item_defidx` | 8 | uint32 | optional |  |

### `AccountActivity`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `activity` | 1 | uint32 | optional |  |
| `mode` | 2 | uint32 | optional |  |
| `map` | 3 | uint32 | optional |  |
| `matchid` | 4 | uint64 | optional |  |

### `TournamentMatchSetup`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `event_id` | 1 | int32 | optional |  |
| `team_id_ct` | 2 | int32 | optional |  |
| `team_id_t` | 3 | int32 | optional |  |
| `event_stage_id` | 4 | int32 | optional |  |

### `ServerHltvInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `tv_udp_port` | 1 | uint32 | optional |  |
| `tv_watch_key` | 2 | uint64 | optional |  |
| `tv_slots` | 3 | uint32 | optional |  |
| `tv_clients` | 4 | uint32 | optional |  |
| `tv_proxies` | 5 | uint32 | optional |  |
| `tv_time` | 6 | uint32 | optional |  |
| `game_type` | 8 | uint32 | optional |  |
| `game_mapgroup` | 9 | string | optional |  |
| `game_map` | 10 | string | optional |  |
| `tv_master_steamid` | 11 | uint64 | optional |  |
| `tv_local_slots` | 12 | uint32 | optional |  |
| `tv_local_clients` | 13 | uint32 | optional |  |
| `tv_local_proxies` | 14 | uint32 | optional |  |
| `tv_relay_slots` | 15 | uint32 | optional |  |
| `tv_relay_clients` | 16 | uint32 | optional |  |
| `tv_relay_proxies` | 17 | uint32 | optional |  |
| `tv_relay_address` | 18 | uint32 | optional |  |
| `tv_relay_port` | 19 | uint32 | optional |  |
| `tv_relay_steamid` | 20 | uint64 | optional |  |
| `flags` | 21 | uint32 | optional |  |

### `IpAddressMask`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `a` | 1 | uint32 | optional |  |
| `b` | 2 | uint32 | optional |  |
| `c` | 3 | uint32 | optional |  |
| `d` | 4 | uint32 | optional |  |
| `bits` | 5 | uint32 | optional |  |
| `token` | 6 | uint32 | optional |  |

### `CMsgCsgoSteamUserStatChange`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ecsgosteamuserstat` | 1 | int32 | optional |  |
| `delta` | 2 | int32 | optional |  |
| `absolute` | 3 | bool | optional |  |

### `XpProgressData`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `xp_points` | 1 | uint32 | optional |  |
| `xp_category` | 2 | int32 | optional |  |

### `MatchEndItemUpdates`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `item_id` | 1 | uint64 | optional |  |
| `item_attr_defidx` | 2 | uint32 | optional |  |
| `item_attr_delta_value` | 3 | uint32 | optional |  |

### `ScoreLeaderboardData`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `quest_id` | 1 | uint64 | optional |  |
| `score` | 2 | uint32 | optional |  |
| `accountentries` | 3 | ScoreLeaderboardData.AccountEntries | repeated |  |
| `matchentries` | 5 | ScoreLeaderboardData.Entry | repeated |  |
| `leaderboard_name` | 6 | string | optional |  |

### `PlayerQuestData`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `quester_account_id` | 1 | uint32 | optional |  |
| `quest_item_data` | 2 | PlayerQuestData.QuestItemData | repeated |  |
| `xp_progress_data` | 3 | [XpProgressData](#xpprogressdata) | repeated |  |
| `time_played` | 4 | uint32 | optional |  |
| `mm_game_mode` | 5 | uint32 | optional |  |
| `item_updates` | 6 | [MatchEndItemUpdates](#matchenditemupdates) | repeated |  |
| `operation_points_eligible` | 7 | bool | optional |  |
| `userstatchanges` | 8 | [CMsgCsgoSteamUserStatChange](#cmsgcsgosteamuserstatchange) | repeated |  |

### `DeepPlayerStatsEntry`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `accountid` | 1 | uint32 | optional |  |
| `match_id` | 2 | uint64 | optional |  |
| `mm_game_mode` | 3 | uint32 | optional |  |
| `mapid` | 4 | uint32 | optional |  |
| `b_starting_ct` | 5 | bool | optional |  |
| `match_outcome` | 6 | uint32 | optional |  |
| `rounds_won` | 7 | uint32 | optional |  |
| `rounds_lost` | 8 | uint32 | optional |  |
| `stat_score` | 9 | uint32 | optional |  |
| `stat_deaths` | 12 | uint32 | optional |  |
| `stat_mvps` | 13 | uint32 | optional |  |
| `enemy_kills` | 14 | uint32 | optional |  |
| `enemy_headshots` | 15 | uint32 | optional |  |
| `enemy_2ks` | 16 | uint32 | optional |  |
| `enemy_3ks` | 17 | uint32 | optional |  |
| `enemy_4ks` | 18 | uint32 | optional |  |
| `total_damage` | 19 | uint32 | optional |  |
| `engagements_entry_count` | 23 | uint32 | optional |  |
| `engagements_entry_wins` | 24 | uint32 | optional |  |
| `engagements_1v1_count` | 25 | uint32 | optional |  |
| `engagements_1v1_wins` | 26 | uint32 | optional |  |
| `engagements_1v2_count` | 27 | uint32 | optional |  |
| `engagements_1v2_wins` | 28 | uint32 | optional |  |
| `utility_count` | 29 | uint32 | optional |  |
| `utility_success` | 30 | uint32 | optional |  |
| `flash_count` | 32 | uint32 | optional |  |
| `flash_success` | 33 | uint32 | optional |  |
| `mates` | 34 | uint32 | repeated |  |

### `DeepPlayerMatchEvent`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `accountid` | 1 | uint32 | optional |  |
| `match_id` | 2 | uint64 | optional |  |
| `event_id` | 3 | uint32 | optional |  |
| `event_type` | 4 | uint32 | optional |  |
| `b_playing_ct` | 5 | bool | optional |  |
| `user_pos_x` | 6 | int32 | optional |  |
| `user_pos_y` | 7 | int32 | optional |  |
| `user_defidx` | 8 | uint32 | optional |  |
| `other_pos_x` | 9 | int32 | optional |  |
| `other_pos_y` | 10 | int32 | optional |  |
| `other_defidx` | 11 | uint32 | optional |  |
| `user_pos_z` | 12 | int32 | optional |  |
| `other_pos_z` | 13 | int32 | optional |  |
| `event_data` | 14 | int32 | optional |  |

### `CMsgGC_ServerQuestUpdateData`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `player_quest_data` | 1 | [PlayerQuestData](#playerquestdata) | repeated |  |
| `binary_data` | 2 | bytes | optional |  |
| `mm_game_mode` | 3 | uint32 | optional |  |
| `missionlbsdata` | 4 | [ScoreLeaderboardData](#scoreleaderboarddata) | optional |  |
| `flags` | 5 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `token` | 1 | uint32 | optional |  |
| `stamp` | 2 | uint32 | optional |  |
| `exchange` | 3 | uint64 | optional |  |
| `retry` | 4 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_GC2ServerReservationUpdate`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `viewers_external_total` | 1 | uint32 | optional |  |
| `viewers_external_steam` | 2 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_MatchmakingStart`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_ids` | 1 | uint32 | repeated |  |
| `game_type` | 2 | uint32 | optional |  |
| `ticket_data` | 3 | string | optional |  |
| `client_version` | 4 | uint32 | optional |  |
| `tournament_match` | 5 | [TournamentMatchSetup](#tournamentmatchsetup) | optional |  |
| `prime_only` | 6 | bool | optional |  |
| `tv_control` | 7 | uint32 | optional |  |
| `lobby_id` | 8 | uint64 | optional |  |

### `CMsgGCCStrike15_v2_MatchmakingStop`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `abandon` | 1 | int32 | optional |  |

### `CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate_Note`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `type` | 1 | int32 | optional |  |
| `region_id` | 2 | int32 | optional |  |
| `region_r` | 3 | float | optional |  |
| `distance` | 4 | float | optional |  |

### `CMsgGCCStrike15_v2_MatchmakingClient2ServerPing`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `gameserverpings` | 1 | [GameServerPing](#gameserverping) | repeated |  |
| `offset_index` | 2 | int32 | optional |  |
| `final_batch` | 3 | int32 | optional |  |
| `data_center_pings` | 4 | [DataCenterPing](#datacenterping) | repeated |  |
| `max_ping` | 5 | uint32 | optional |  |
| `test_token` | 6 | fixed32 | optional |  |
| `search_key` | 7 | bytes | optional |  |
| `notes` | 8 | [CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate_Note](#cmsggccstrike15_v2_matchmakinggc2clientupdate_note) | repeated |  |
| `debug_message` | 9 | string | optional |  |

### `CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `matchmaking` | 1 | int32 | optional |  |
| `waiting_account_id_sessions` | 2 | uint32 | repeated |  |
| `error` | 3 | string | optional |  |
| `ongoingmatch_account_id_sessions` | 6 | uint32 | repeated |  |
| `global_stats` | 7 | [GlobalStatistics](#globalstatistics) | optional |  |
| `failping_account_id_sessions` | 8 | uint32 | repeated |  |
| `penalty_account_id_sessions` | 9 | uint32 | repeated |  |
| `failready_account_id_sessions` | 10 | uint32 | repeated |  |
| `vacbanned_account_id_sessions` | 11 | uint32 | repeated |  |
| `server_ipaddress_mask` | 12 | [IpAddressMask](#ipaddressmask) | optional |  |
| `notes` | 13 | [CMsgGCCStrike15_v2_MatchmakingGC2ClientUpdate_Note](#cmsggccstrike15_v2_matchmakinggc2clientupdate_note) | repeated |  |
| `penalty_account_id_sessions_green` | 14 | uint32 | repeated |  |
| `insufficientlevel_sessions` | 15 | uint32 | repeated |  |
| `vsncheck_account_id_sessions` | 16 | uint32 | repeated |  |
| `launcher_mismatch_sessions` | 17 | uint32 | repeated |  |
| `insecure_account_id_sessions` | 18 | uint32 | repeated |  |

### `CDataGCCStrike15_v2_TournamentMatchDraft`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `event_id` | 1 | int32 | optional |  |
| `event_stage_id` | 2 | int32 | optional |  |
| `team_id_0` | 3 | int32 | optional |  |
| `team_id_1` | 4 | int32 | optional |  |
| `maps_count` | 5 | int32 | optional |  |
| `maps_current` | 6 | int32 | optional |  |
| `team_id_start` | 7 | int32 | optional |  |
| `team_id_veto1` | 8 | int32 | optional |  |
| `team_id_pickn` | 9 | int32 | optional |  |
| `drafts` | 10 | CDataGCCStrike15_v2_TournamentMatchDraft.Entry | repeated |  |
| `vote_mapid_0` | 11 | int32 | repeated |  |
| `vote_mapid_1` | 12 | int32 | repeated |  |
| `vote_mapid_2` | 13 | int32 | repeated |  |
| `vote_mapid_3` | 14 | int32 | repeated |  |
| `vote_mapid_4` | 15 | int32 | repeated |  |
| `vote_mapid_5` | 16 | int32 | repeated |  |
| `vote_starting_side` | 17 | int32 | repeated |  |
| `vote_phase` | 18 | int32 | optional |  |
| `vote_phase_start` | 19 | float | optional |  |
| `vote_phase_length` | 20 | float | optional |  |

### `CPreMatchInfoData`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `predictions_pct` | 1 | int32 | optional |  |
| `draft` | 4 | [CDataGCCStrike15_v2_TournamentMatchDraft](#cdatagccstrike15_v2_tournamentmatchdraft) | optional |  |
| `stats` | 5 | CPreMatchInfoData.TeamStats | repeated |  |
| `wins` | 6 | int32 | repeated |  |

### `CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_ids` | 1 | uint32 | repeated |  |
| `game_type` | 2 | uint32 | optional |  |
| `match_id` | 3 | uint64 | optional |  |
| `server_version` | 4 | uint32 | optional |  |
| `rankings` | 5 | [PlayerRankingInfo](#playerrankinginfo) | repeated |  |
| `encryption_key` | 6 | uint64 | optional |  |
| `encryption_key_pub` | 7 | uint64 | optional |  |
| `party_ids` | 8 | uint32 | repeated |  |
| `whitelist` | 9 | [IpAddressMask](#ipaddressmask) | repeated |  |
| `tv_master_steamid` | 10 | uint64 | optional |  |
| `tournament_event` | 11 | [TournamentEvent](#tournamentevent) | optional |  |
| `tournament_teams` | 12 | [TournamentTeam](#tournamentteam) | repeated |  |
| `tournament_casters_account_ids` | 13 | uint32 | repeated |  |
| `tv_relay_steamid` | 14 | uint64 | optional |  |
| `pre_match_data` | 15 | [CPreMatchInfoData](#cprematchinfodata) | optional |  |
| `tv_control` | 17 | uint32 | optional |  |
| `flags` | 18 | uint32 | optional |  |
| `op_var_values` | 19 | [OperationalVarValue](#operationalvarvalue) | repeated |  |
| `socache_control` | 20 | uint32 | optional |  |
| `teammate_colors` | 21 | int32 | repeated |  |
| `match_id_additional` | 22 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_MatchmakingServerReservationResponse`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `reservationid` | 1 | uint64 | optional |  |
| `reservation` | 2 | [CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve](#cmsggccstrike15_v2_matchmakinggc2serverreserve) | optional |  |
| `map` | 3 | string | optional |  |
| `gc_reservation_sent` | 4 | uint64 | optional |  |
| `server_version` | 5 | uint32 | optional |  |
| `tv_info` | 6 | [ServerHltvInfo](#serverhltvinfo) | optional |  |
| `reward_player_accounts` | 7 | uint32 | repeated |  |
| `idle_player_accounts` | 8 | uint32 | repeated |  |
| `reward_item_attr_def_idx` | 9 | uint32 | optional |  |
| `reward_item_attr_value` | 10 | uint32 | optional |  |
| `reward_item_attr_reward_idx` | 11 | uint32 | optional |  |
| `reward_drop_list` | 12 | uint32 | optional |  |
| `tournament_tag` | 13 | string | optional |  |
| `legacy_steamdatagram_port` | 14 | uint32 | optional |  |
| `test_token` | 15 | fixed32 | optional |  |
| `flags` | 16 | uint32 | optional |  |
| `steamdatagram_routing` | 17 | uint32 | optional |  |
| `system_load` | 18 | uint32 | optional |  |
| `cpus_online` | 19 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `serverid` | 1 | uint64 | optional |  |
| `direct_udp_ip` | 2 | uint32 | optional |  |
| `direct_udp_port` | 3 | uint32 | optional |  |
| `reservationid` | 4 | uint64 | optional |  |
| `reservation` | 5 | [CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve](#cmsggccstrike15_v2_matchmakinggc2serverreserve) | optional |  |
| `map` | 6 | string | optional |  |
| `server_address` | 7 | string | optional |  |
| `gs_ping` | 8 | [DataCenterPing](#datacenterping) | optional |  |
| `gs_location_id` | 9 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_MatchmakingServerRoundStats`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `reservationid` | 1 | uint64 | optional |  |
| `reservation` | 2 | [CMsgGCCStrike15_v2_MatchmakingGC2ServerReserve](#cmsggccstrike15_v2_matchmakinggc2serverreserve) | optional |  |
| `map` | 3 | string | optional |  |
| `round` | 4 | int32 | optional |  |
| `kills` | 5 | int32 | repeated |  |
| `assists` | 6 | int32 | repeated |  |
| `deaths` | 7 | int32 | repeated |  |
| `scores` | 8 | int32 | repeated |  |
| `pings` | 9 | int32 | repeated |  |
| `round_result` | 10 | int32 | optional |  |
| `match_result` | 11 | int32 | optional |  |
| `team_scores` | 12 | int32 | repeated |  |
| `confirm` | 13 | [CMsgGCCStrike15_v2_MatchmakingGC2ServerConfirm](#cmsggccstrike15_v2_matchmakinggc2serverconfirm) | optional |  |
| `reservation_stage` | 14 | int32 | optional |  |
| `match_duration` | 15 | int32 | optional |  |
| `enemy_kills` | 16 | int32 | repeated |  |
| `enemy_headshots` | 17 | int32 | repeated |  |
| `enemy_3ks` | 18 | int32 | repeated |  |
| `enemy_4ks` | 19 | int32 | repeated |  |
| `enemy_5ks` | 20 | int32 | repeated |  |
| `mvps` | 21 | int32 | repeated |  |
| `spectators_count` | 22 | uint32 | optional |  |
| `spectators_count_tv` | 23 | uint32 | optional |  |
| `spectators_count_lnk` | 24 | uint32 | optional |  |
| `enemy_kills_agg` | 25 | int32 | repeated |  |
| `drop_info` | 26 | CMsgGCCStrike15_v2_MatchmakingServerRoundStats.DropInfo | optional |  |
| `b_switched_teams` | 27 | bool | optional |  |
| `enemy_2ks` | 28 | int32 | repeated |  |
| `player_spawned` | 29 | int32 | repeated |  |
| `team_spawn_count` | 30 | int32 | repeated |  |
| `max_rounds` | 31 | uint32 | optional |  |
| `map_id` | 32 | int32 | optional |  |

### `CMsgGCCStrike15_v2_MatchmakingClient2GCHello`

### `CMsgGCCStrike15_v2_MatchmakingGC2ClientHello`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `ongoingmatch` | 2 | [CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve](#cmsggccstrike15_v2_matchmakinggc2clientreserve) | optional |  |
| `global_stats` | 3 | [GlobalStatistics](#globalstatistics) | optional |  |
| `penalty_seconds` | 4 | uint32 | optional |  |
| `penalty_reason` | 5 | uint32 | optional |  |
| `vac_banned` | 6 | int32 | optional |  |
| `ranking` | 7 | [PlayerRankingInfo](#playerrankinginfo) | optional |  |
| `commendation` | 8 | [PlayerCommendationInfo](#playercommendationinfo) | optional |  |
| `medals` | 9 | [PlayerMedalsInfo](#playermedalsinfo) | optional |  |
| `my_current_event` | 10 | [TournamentEvent](#tournamentevent) | optional |  |
| `my_current_event_teams` | 11 | [TournamentTeam](#tournamentteam) | repeated |  |
| `my_current_team` | 12 | [TournamentTeam](#tournamentteam) | optional |  |
| `my_current_event_stages` | 13 | [TournamentEvent](#tournamentevent) | repeated |  |
| `survey_vote` | 14 | uint32 | optional |  |
| `activity` | 15 | [AccountActivity](#accountactivity) | optional |  |
| `player_level` | 17 | int32 | optional |  |
| `player_cur_xp` | 18 | int32 | optional |  |
| `player_xp_bonus_flags` | 19 | int32 | optional |  |
| `rankings` | 20 | [PlayerRankingInfo](#playerrankinginfo) | repeated |  |
| `owcaseid` | 21 | uint64 | optional |  |

### `CMsgGCCStrike15_v2_AccountPrivacySettings`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `settings` | 1 | CMsgGCCStrike15_v2_AccountPrivacySettings.Setting | repeated |  |

### `CMsgGCCStrike15_v2_MatchmakingGC2ClientAbandon`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `abandoned_match` | 2 | [CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve](#cmsggccstrike15_v2_matchmakinggc2clientreserve) | optional |  |
| `penalty_seconds` | 3 | uint32 | optional |  |
| `penalty_reason` | 4 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_ClientGCRankUpdate`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `rankings` | 1 | [PlayerRankingInfo](#playerrankinginfo) | repeated |  |

### `CMsgGCCStrike15_v2_MatchmakingOperator2GCBlogUpdate`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `main_post_url` | 1 | string | optional |  |

### `CMsgGCCStrike15_v2_ServerNotificationForUserPenalty`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `reason` | 2 | uint32 | optional |  |
| `seconds` | 3 | uint32 | optional |  |
| `communication_cooldown` | 4 | bool | optional |  |

### `CMsgGCCStrike15_v2_ClientReportPlayer`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `rpt_aimbot` | 2 | uint32 | optional |  |
| `rpt_wallhack` | 3 | uint32 | optional |  |
| `rpt_speedhack` | 4 | uint32 | optional |  |
| `rpt_teamharm` | 5 | uint32 | optional |  |
| `rpt_textabuse` | 6 | uint32 | optional |  |
| `rpt_voiceabuse` | 7 | uint32 | optional |  |
| `match_id` | 8 | uint64 | optional |  |
| `report_from_demo` | 9 | bool | optional |  |

### `CMsgGCCStrike15_v2_ClientCommendPlayer`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `match_id` | 8 | uint64 | optional |  |
| `commendation` | 9 | [PlayerCommendationInfo](#playercommendationinfo) | optional |  |
| `tokens` | 10 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_ClientReportServer`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `rpt_poorperf` | 1 | uint32 | optional |  |
| `rpt_abusivemodels` | 2 | uint32 | optional |  |
| `rpt_badmotd` | 3 | uint32 | optional |  |
| `rpt_listingabuse` | 4 | uint32 | optional |  |
| `rpt_inventoryabuse` | 5 | uint32 | optional |  |
| `match_id` | 8 | uint64 | optional |  |

### `CMsgGCCStrike15_v2_ClientReportResponse`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `confirmation_id` | 1 | uint64 | optional |  |
| `account_id` | 2 | uint32 | optional |  |
| `server_ip` | 3 | uint32 | optional |  |
| `response_type` | 4 | uint32 | optional |  |
| `response_result` | 5 | uint32 | optional |  |
| `tokens` | 6 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_ClientRequestWatchInfoFriends`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `request_id` | 1 | uint32 | optional |  |
| `account_ids` | 2 | uint32 | repeated |  |
| `serverid` | 3 | uint64 | optional |  |
| `matchid` | 4 | uint64 | optional |  |
| `client_launcher` | 5 | uint32 | optional |  |
| `data_center_pings` | 6 | [DataCenterPing](#datacenterping) | repeated |  |

### `WatchableMatchInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `server_ip` | 1 | uint32 | optional |  |
| `tv_port` | 2 | uint32 | optional |  |
| `tv_spectators` | 3 | uint32 | optional |  |
| `tv_time` | 4 | uint32 | optional |  |
| `tv_watch_password` | 5 | bytes | optional |  |
| `cl_decryptdata_key` | 6 | uint64 | optional |  |
| `cl_decryptdata_key_pub` | 7 | uint64 | optional |  |
| `game_type` | 8 | uint32 | optional |  |
| `game_mapgroup` | 9 | string | optional |  |
| `game_map` | 10 | string | optional |  |
| `server_id` | 11 | uint64 | optional |  |
| `match_id` | 12 | uint64 | optional |  |
| `reservation_id` | 13 | uint64 | optional |  |

### `CMsgGCCStrike15_v2_ClientRequestJoinFriendData`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `version` | 1 | uint32 | optional |  |
| `account_id` | 2 | uint32 | optional |  |
| `join_token` | 3 | uint32 | optional |  |
| `join_ipp` | 4 | uint32 | optional |  |
| `res` | 5 | [CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve](#cmsggccstrike15_v2_matchmakinggc2clientreserve) | optional |  |
| `errormsg` | 6 | string | optional |  |
| `is_local_server` | 7 | bool | optional |  |

### `CMsgGCCStrike15_v2_ClientRequestJoinServerData`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `version` | 1 | uint32 | optional |  |
| `account_id` | 2 | uint32 | optional |  |
| `serverid` | 3 | uint64 | optional |  |
| `server_ip` | 4 | uint32 | optional |  |
| `server_port` | 5 | uint32 | optional |  |
| `res` | 6 | [CMsgGCCStrike15_v2_MatchmakingGC2ClientReserve](#cmsggccstrike15_v2_matchmakinggc2clientreserve) | optional |  |
| `errormsg` | 7 | string | optional |  |

### `CMsgGCCstrike15_v2_ClientRedeemMissionReward`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `campaign_id` | 1 | uint32 | optional |  |
| `redeem_id` | 2 | uint32 | optional |  |
| `redeemable_balance` | 3 | uint32 | optional |  |
| `expected_cost` | 4 | uint32 | optional |  |
| `bid_control` | 5 | int32 | optional |  |

### `CMsgGCCstrike15_v2_ClientRedeemFreeReward`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `generation_time` | 1 | uint32 | optional |  |
| `redeemable_balance` | 2 | uint32 | optional |  |
| `items` | 3 | uint64 | repeated |  |

### `CMsgGCCstrike15_v2_GC2ServerNotifyXPRewarded`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `xp_progress_data` | 1 | [XpProgressData](#xpprogressdata) | repeated |  |
| `account_id` | 2 | uint32 | optional |  |
| `current_xp` | 3 | uint32 | optional |  |
| `current_level` | 4 | uint32 | optional |  |
| `upgraded_defidx` | 5 | uint32 | optional |  |
| `operation_points_awarded` | 6 | uint32 | optional |  |
| `free_rewards` | 7 | uint32 | optional |  |
| `xp_trail_remaining` | 8 | uint32 | optional |  |
| `xp_trail_xp_needed` | 9 | int32 | optional |  |
| `xp_trail_level` | 10 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_ClientNetworkConfig`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `data` | 1 | bytes | optional |  |

### `CMsgGCCStrike15_ClientDeepStats`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `range` | 2 | CMsgGCCStrike15_ClientDeepStats.DeepStatsRange | optional |  |
| `matches` | 3 | CMsgGCCStrike15_ClientDeepStats.DeepStatsMatch | repeated |  |

### `CMsgGCCStrike15_v2_WatchInfoUsers`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `request_id` | 1 | uint32 | optional |  |
| `account_ids` | 2 | uint32 | repeated |  |
| `watchable_match_infos` | 3 | [WatchableMatchInfo](#watchablematchinfo) | repeated |  |
| `extended_timeout` | 5 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_ClientRequestPlayersProfile`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `request_id__deprecated` | 1 | uint32 | optional |  |
| `account_ids__deprecated` | 2 | uint32 | repeated |  |
| `account_id` | 3 | uint32 | optional |  |
| `request_level` | 4 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_PlayersProfile`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `request_id` | 1 | uint32 | optional |  |
| `account_profiles` | 2 | [CMsgGCCStrike15_v2_MatchmakingGC2ClientHello](#cmsggccstrike15_v2_matchmakinggc2clienthello) | repeated |  |

### `CMsgGCCStrike15_v2_PremierSeasonSummary`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `season_id` | 2 | uint32 | optional |  |
| `data_per_week` | 3 | CMsgGCCStrike15_v2_PremierSeasonSummary.DataPerWeek | repeated |  |
| `data_per_map` | 4 | CMsgGCCStrike15_v2_PremierSeasonSummary.DataPerMap | repeated |  |

### `CMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `caseid` | 1 | uint64 | optional |  |
| `suspectid` | 3 | uint32 | optional |  |
| `fractionid` | 4 | uint32 | optional |  |
| `rpt_aimbot` | 5 | uint32 | optional |  |
| `rpt_wallhack` | 6 | uint32 | optional |  |
| `rpt_speedhack` | 7 | uint32 | optional |  |
| `rpt_teamharm` | 8 | uint32 | optional |  |
| `reason` | 9 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `caseid` | 1 | uint64 | optional |  |
| `caseurl` | 2 | string | optional |  |
| `verdict` | 3 | uint32 | optional |  |
| `timestamp` | 4 | uint32 | optional |  |
| `throttleseconds` | 5 | uint32 | optional |  |
| `suspectid` | 6 | uint32 | optional |  |
| `fractionid` | 7 | uint32 | optional |  |
| `numrounds` | 8 | uint32 | optional |  |
| `fractionrounds` | 9 | uint32 | optional |  |
| `streakconvictions` | 10 | int32 | optional |  |
| `reason` | 11 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_PlayerOverwatchCaseStatus`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `caseid` | 1 | uint64 | optional |  |
| `statusid` | 2 | uint32 | optional |  |

### `CClientHeaderOverwatchEvidence`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `accountid` | 1 | uint32 | optional |  |
| `caseid` | 2 | uint64 | optional |  |

### `CMsgGCCStrike15_v2_GC2ClientTextMsg`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `id` | 1 | uint32 | optional |  |
| `type` | 2 | uint32 | optional |  |
| `payload` | 3 | bytes | optional |  |

### `CMsgGCCStrike15_v2_Client2GCTextMsg`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `id` | 1 | uint32 | optional |  |
| `args` | 2 | bytes | repeated |  |

### `CMsgGCCStrike15_v2_MatchEndRunRewardDrops`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `serverinfo` | 3 | [CMsgGCCStrike15_v2_MatchmakingServerReservationResponse](#cmsggccstrike15_v2_matchmakingserverreservationresponse) | optional |  |
| `match_end_quest_data` | 4 | [CMsgGC_ServerQuestUpdateData](#cmsggc_serverquestupdatedata) | optional |  |

### `CEconItemPreviewDataBlock`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `accountid` | 1 | uint32 | optional |  |
| `itemid` | 2 | uint64 | optional |  |
| `defindex` | 3 | uint32 | optional |  |
| `paintindex` | 4 | uint32 | optional |  |
| `rarity` | 5 | uint32 | optional |  |
| `quality` | 6 | uint32 | optional |  |
| `paintwear` | 7 | uint32 | optional |  |
| `paintseed` | 8 | uint32 | optional |  |
| `killeaterscoretype` | 9 | uint32 | optional |  |
| `killeatervalue` | 10 | uint32 | optional |  |
| `customname` | 11 | string | optional |  |
| `stickers` | 12 | CEconItemPreviewDataBlock.Sticker | repeated |  |
| `inventory` | 13 | uint32 | optional |  |
| `origin` | 14 | uint32 | optional |  |
| `questid` | 15 | uint32 | optional |  |
| `dropreason` | 16 | uint32 | optional |  |
| `musicindex` | 17 | uint32 | optional |  |
| `entindex` | 18 | int32 | optional |  |
| `petindex` | 19 | uint32 | optional |  |
| `keychains` | 20 | CEconItemPreviewDataBlock.Sticker | repeated |  |
| `style` | 21 | uint32 | optional |  |
| `variations` | 22 | CEconItemPreviewDataBlock.Sticker | repeated |  |
| `upgrade_level` | 23 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_MatchEndRewardDropsNotification`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `iteminfo` | 6 | [CEconItemPreviewDataBlock](#ceconitempreviewdatablock) | optional |  |

### `CMsgItemAcknowledged`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `iteminfo` | 1 | [CEconItemPreviewDataBlock](#ceconitempreviewdatablock) | optional |  |

### `CMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockRequest`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `param_s` | 1 | uint64 | optional |  |
| `param_a` | 2 | uint64 | optional |  |
| `param_d` | 3 | uint64 | optional |  |
| `param_m` | 4 | uint64 | optional |  |

### `CMsgGCCStrike15_v2_Client2GCEconPreviewDataBlockResponse`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `iteminfo` | 1 | [CEconItemPreviewDataBlock](#ceconitempreviewdatablock) | optional |  |

### `CMsgGCCStrike15_v2_MatchListRequestCurrentLiveGames`

### `CMsgGCCStrike15_v2_MatchListRequestLiveGameForUser`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `accountid` | 1 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_MatchListRequestRecentUserGames`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `accountid` | 1 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_MatchListRequestTournamentGames`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `eventid` | 1 | int32 | optional |  |

### `CMsgGCCStrike15_v2_MatchListRequestFullGameInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `matchid` | 1 | uint64 | optional |  |
| `outcomeid` | 2 | uint64 | optional |  |
| `token` | 3 | uint32 | optional |  |

### `CDataGCCStrike15_v2_MatchInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `matchid` | 1 | uint64 | optional |  |
| `matchtime` | 2 | uint32 | optional |  |
| `watchablematchinfo` | 3 | [WatchableMatchInfo](#watchablematchinfo) | optional |  |
| `roundstats_legacy` | 4 | [CMsgGCCStrike15_v2_MatchmakingServerRoundStats](#cmsggccstrike15_v2_matchmakingserverroundstats) | optional |  |
| `roundstatsall` | 5 | [CMsgGCCStrike15_v2_MatchmakingServerRoundStats](#cmsggccstrike15_v2_matchmakingserverroundstats) | repeated |  |

### `CDataGCCStrike15_v2_TournamentGroupTeam`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `team_id` | 1 | int32 | optional |  |
| `score` | 2 | int32 | optional |  |
| `correctpick` | 3 | bool | optional |  |

### `CDataGCCStrike15_v2_TournamentGroup`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `groupid` | 1 | uint32 | optional |  |
| `name` | 2 | string | optional |  |
| `desc` | 3 | string | optional |  |
| `picks__deprecated` | 4 | uint32 | optional |  |
| `teams` | 5 | [CDataGCCStrike15_v2_TournamentGroupTeam](#cdatagccstrike15_v2_tournamentgroupteam) | repeated |  |
| `stage_ids` | 6 | int32 | repeated |  |
| `picklockuntiltime` | 7 | uint32 | optional |  |
| `pickableteams` | 8 | uint32 | optional |  |
| `points_per_pick` | 9 | uint32 | optional |  |
| `picks` | 10 | CDataGCCStrike15_v2_TournamentGroup.Picks | repeated |  |

### `CDataGCCStrike15_v2_TournamentSection`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `sectionid` | 1 | uint32 | optional |  |
| `name` | 2 | string | optional |  |
| `desc` | 3 | string | optional |  |
| `groups` | 4 | [CDataGCCStrike15_v2_TournamentGroup](#cdatagccstrike15_v2_tournamentgroup) | repeated |  |

### `CDataGCCStrike15_v2_TournamentInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `sections` | 1 | [CDataGCCStrike15_v2_TournamentSection](#cdatagccstrike15_v2_tournamentsection) | repeated |  |
| `tournament_event` | 2 | [TournamentEvent](#tournamentevent) | optional |  |
| `tournament_teams` | 3 | [TournamentTeam](#tournamentteam) | repeated |  |

### `CMsgGCCStrike15_v2_MatchList`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `msgrequestid` | 1 | uint32 | optional |  |
| `accountid` | 2 | uint32 | optional |  |
| `servertime` | 3 | uint32 | optional |  |
| `matches` | 4 | [CDataGCCStrike15_v2_MatchInfo](#cdatagccstrike15_v2_matchinfo) | repeated |  |
| `streams` | 5 | [TournamentTeam](#tournamentteam) | repeated |  |
| `tournamentinfo` | 6 | [CDataGCCStrike15_v2_TournamentInfo](#cdatagccstrike15_v2_tournamentinfo) | optional |  |

### `CMsgGCCStrike15_v2_MatchListTournamentOperatorMgmt`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `eventid` | 1 | int32 | optional |  |
| `matches` | 2 | [CDataGCCStrike15_v2_MatchInfo](#cdatagccstrike15_v2_matchinfo) | repeated |  |
| `accountid` | 3 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_Predictions`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `event_id` | 1 | uint32 | optional |  |
| `group_match_team_picks` | 2 | CMsgGCCStrike15_v2_Predictions.GroupMatchTeamPick | repeated |  |

### `CMsgGCCStrike15_v2_Fantasy`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `event_id` | 1 | uint32 | optional |  |
| `teams` | 2 | CMsgGCCStrike15_v2_Fantasy.FantasyTeam | repeated |  |

### `CAttribute_String`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `value` | 1 | string | optional |  |

### `CMsgLegacySource1ClientWelcome`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `version` | 1 | uint32 | optional |  |
| `game_data` | 2 | bytes | optional |  |
| `outofdate_subscribed_caches` | 3 | CMsgSOCacheSubscribed | repeated |  |
| `uptodate_subscribed_caches` | 4 | CMsgSOCacheSubscriptionCheck | repeated |  |
| `location` | 5 | CMsgLegacySource1ClientWelcome.Location | optional |  |
| `game_data2` | 6 | bytes | optional |  |
| `rtime32_gc_welcome_timestamp` | 7 | uint32 | optional |  |
| `currency` | 8 | uint32 | optional |  |
| `balance` | 9 | uint32 | optional |  |
| `balance_url` | 10 | string | optional |  |
| `txn_country_code` | 11 | string | optional |  |

### `CMsgCStrike15Welcome`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `store_item_hash` | 5 | uint32 | optional |  |
| `timeplayedconsecutively` | 6 | uint32 | optional |  |
| `time_first_played` | 10 | uint32 | optional |  |
| `last_time_played` | 12 | uint32 | optional |  |
| `last_ip_address` | 13 | uint32 | optional |  |
| `gscookieid` | 18 | uint64 | optional |  |
| `uniqueid` | 19 | uint64 | optional |  |

### `CMsgGCCStrike15_v2_ClientVarValueNotificationInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `value_name` | 1 | string | optional |  |
| `value_int` | 2 | int32 | optional |  |
| `server_addr` | 3 | uint32 | optional |  |
| `server_port` | 4 | uint32 | optional |  |
| `choked_blocks` | 5 | string | repeated |  |

### `CMsgGCCStrike15_v2_ServerVarValueNotificationInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `accountid` | 1 | uint32 | optional |  |
| `viewangles` | 2 | uint32 | repeated |  |
| `type` | 3 | uint32 | optional |  |
| `userdata` | 4 | uint32 | repeated |  |

### `CMsgGCCStrike15_v2_GiftsLeaderboardRequest`

### `CMsgGCCStrike15_v2_GiftsLeaderboardResponse`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `servertime` | 1 | uint32 | optional |  |
| `time_period_seconds` | 2 | uint32 | optional |  |
| `total_gifts_given` | 3 | uint32 | optional |  |
| `total_givers` | 4 | uint32 | optional |  |
| `entries` | 5 | CMsgGCCStrike15_v2_GiftsLeaderboardResponse.GiftLeaderboardEntry | repeated |  |

### `CMsgGCCStrike15_v2_ClientSubmitSurveyVote`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `survey_id` | 1 | uint32 | optional |  |
| `vote` | 2 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_Server2GCClientValidate`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `accountid` | 1 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_GC2ClientTournamentInfo`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `eventid` | 1 | uint32 | optional |  |
| `stageid` | 2 | uint32 | optional |  |
| `game_type` | 3 | uint32 | optional |  |
| `teamids` | 4 | uint32 | repeated |  |

### `CSOEconCoupon`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `entryid` | 1 | uint32 | optional |  |
| `defidx` | 2 | uint32 | optional |  |
| `expiration_date` | 3 | fixed32 | optional |  |

### `CSOAccountItemPersonalStore`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `generation_time` | 1 | uint32 | optional |  |
| `redeemable_balance` | 2 | uint32 | optional |  |
| `items` | 3 | uint64 | repeated |  |

### `CSOAccountXpShop`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `generation_time` | 1 | uint32 | optional |  |
| `redeemable_balance` | 2 | uint32 | optional |  |
| `xp_tracks` | 3 | uint32 | repeated |  |

### `CSOAccountXpShopBids`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `campaign_id` | 1 | uint32 | optional |  |
| `redeem_id` | 2 | uint32 | optional |  |
| `expected_cost` | 3 | uint32 | optional |  |
| `generation_time` | 4 | uint32 | optional |  |

### `CSOVolatileItemOffer`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `defidx` | 1 | uint32 | optional |  |
| `faux_itemid` | 2 | uint64 | repeated |  |
| `generation_time` | 3 | uint32 | repeated |  |

### `CSOVolatileItemClaimedRewards`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `defidx` | 1 | uint32 | optional |  |
| `reward` | 2 | uint32 | repeated |  |
| `generation_time` | 3 | uint32 | repeated |  |

### `CSOAccountKeychainRemoveToolCharges`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `charges` | 1 | uint32 | optional |  |

### `CSOQuestProgress`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `questid` | 1 | uint32 | optional |  |
| `points_remaining` | 2 | uint32 | optional |  |
| `bonus_points` | 3 | uint32 | optional |  |

### `CSOAccountSeasonalOperation`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `season_value` | 1 | uint32 | optional |  |
| `tier_unlocked` | 2 | uint32 | optional |  |
| `premium_tiers` | 3 | uint32 | optional |  |
| `mission_id` | 4 | uint32 | optional |  |
| `missions_completed` | 5 | uint32 | optional |  |
| `redeemable_balance` | 6 | uint32 | optional |  |
| `season_pass_time` | 7 | uint32 | optional |  |

### `CSOAccountRecurringSubscription`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `time_next_cycle` | 1 | uint32 | optional |  |
| `time_initiated` | 2 | uint32 | optional |  |

### `CSOGameAccountSteamChina`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `time_last_update` | 1 | uint32 | optional |  |
| `time_comms_ban` | 2 | uint32 | optional |  |
| `time_play_ban` | 3 | uint32 | optional |  |

### `CSOPersonaDataPublic`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `player_level` | 1 | int32 | optional |  |
| `commendation` | 2 | [PlayerCommendationInfo](#playercommendationinfo) | optional |  |
| `elevated_state` | 3 | bool | optional |  |
| `xp_trail_timestamp_refresh` | 4 | uint32 | optional |  |
| `xp_trail_level` | 5 | uint32 | optional |  |

### `CSOAccountRecurringMission`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `mission_id` | 2 | uint32 | optional |  |
| `period` | 3 | uint32 | optional |  |
| `progress` | 4 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_GC2ClientNotifyXPShop`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `prematch` | 1 | [CSOAccountXpShop](#csoaccountxpshop) | optional |  |
| `postmatch` | 2 | [CSOAccountXpShop](#csoaccountxpshop) | optional |  |
| `current_xp` | 3 | uint32 | optional |  |
| `current_level` | 4 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_Client2GcAckXPShopTracks`

### `CMsgGCCStrike15_v2_MatchmakingGC2ClientSearchStats`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `gs_location_id` | 1 | uint32 | optional |  |
| `data_center_id` | 2 | uint32 | optional |  |
| `num_locked_in` | 3 | uint32 | optional |  |
| `num_found_nearby` | 4 | uint32 | optional |  |
| `note_level` | 5 | uint32 | optional |  |

### `CMsgGC_GlobalGame_Subscribe`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ticket` | 1 | uint64 | optional |  |

### `CMsgGC_GlobalGame_Unsubscribe`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `timeleft` | 1 | int32 | optional |  |

### `CMsgGC_GlobalGame_Play`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ticket` | 1 | uint64 | optional |  |
| `gametimems` | 2 | uint32 | optional |  |
| `msperpoint` | 3 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_AcknowledgePenalty`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `acknowledged` | 1 | int32 | optional |  |

### `CMsgGCCStrike15_v2_Client2GCRequestPrestigeCoin`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `defindex` | 1 | uint32 | optional |  |
| `upgradeid` | 2 | uint64 | optional |  |
| `hours` | 3 | uint32 | optional |  |
| `prestigetime` | 4 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_Client2GCStreamUnlock`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ticket` | 1 | uint64 | optional |  |
| `os` | 2 | int32 | optional |  |

### `CMsgGCCStrike15_v2_ClientToGCRequestElevate`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `stage` | 1 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_ClientToGCChat`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `match_id` | 1 | uint64 | optional |  |
| `text` | 2 | string | optional |  |

### `CMsgGCCStrike15_v2_GCToClientChat`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `account_id` | 1 | uint32 | optional |  |
| `text` | 2 | string | optional |  |

### `CMsgGCCStrike15_v2_ClientAuthKeyCode`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `eventid` | 1 | uint32 | optional |  |
| `code` | 2 | string | optional |  |

### `CMsgGCCStrike15_GotvSyncPacket`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `data` | 1 | CEngineGotvSyncPacket | optional |  |

### `PlayerDecalDigitalSignature`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `signature` | 1 | bytes | optional |  |
| `accountid` | 2 | uint32 | optional |  |
| `rtime` | 3 | uint32 | optional |  |
| `endpos` | 4 | float | repeated |  |
| `startpos` | 5 | float | repeated |  |
| `left` | 6 | float | repeated |  |
| `tx_defidx` | 7 | uint32 | optional |  |
| `entindex` | 8 | int32 | optional |  |
| `hitbox` | 9 | uint32 | optional |  |
| `creationtime` | 10 | float | optional |  |
| `equipslot` | 11 | uint32 | optional |  |
| `trace_id` | 12 | uint32 | optional |  |
| `normal` | 13 | float | repeated |  |
| `tint_id` | 14 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_ClientPlayerDecalSign`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `data` | 1 | [PlayerDecalDigitalSignature](#playerdecaldigitalsignature) | optional |  |
| `itemid` | 2 | uint64 | optional |  |

### `CMsgGCCStrike15_v2_BetaEnrollment`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `eresult` | 1 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_ClientLogonFatalError`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `errorcode` | 1 | uint32 | optional |  |
| `message` | 2 | string | optional |  |
| `country` | 3 | string | optional |  |

### `CMsgGCCStrike15_v2_ClientPollState`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `pollid` | 1 | uint32 | optional |  |
| `names` | 2 | string | repeated |  |
| `values` | 3 | int32 | repeated |  |

### `CMsgGCCStrike15_v2_Party_Register`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `id` | 1 | uint32 | optional |  |
| `ver` | 2 | uint32 | optional |  |
| `apr` | 3 | uint32 | optional |  |
| `ark` | 4 | uint32 | optional |  |
| `nby` | 5 | uint32 | optional |  |
| `grp` | 6 | uint32 | optional |  |
| `slots` | 7 | uint32 | optional |  |
| `launcher` | 8 | uint32 | optional |  |
| `game_type` | 9 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_Party_Search`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `ver` | 1 | uint32 | optional |  |
| `apr` | 2 | uint32 | optional |  |
| `ark` | 3 | uint32 | optional |  |
| `grps` | 4 | uint32 | repeated |  |
| `launcher` | 5 | uint32 | optional |  |
| `game_type` | 6 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_Party_SearchResults`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `entries` | 1 | CMsgGCCStrike15_v2_Party_SearchResults.Entry | repeated |  |

### `CMsgGCCStrike15_v2_Party_Invite`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `accountid` | 1 | uint32 | optional |  |
| `lobbyid` | 2 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_Account_RequestCoPlays`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `players` | 1 | CMsgGCCStrike15_v2_Account_RequestCoPlays.Player | repeated |  |
| `servertime` | 2 | uint32 | optional |  |

### `CMsgGCCStrike15_v2_ClientToGCRequestTicket`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `authorized_steam_id` | 1 | fixed64 | optional |  |
| `authorized_public_ip` | 2 | fixed32 | optional |  |
| `gameserver_steam_id` | 3 | fixed64 | optional |  |
| `gameserver_sdr_routing` | 5 | string | optional |  |

### `CMsgGCToClientSteamDatagramTicket`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `serialized_ticket` | 16 | bytes | optional |  |

### `CMsgGCCStrike15_v2_ClientRequestOffers`

### `CMsgGCCStrike15_v2_ClientRequestSouvenir`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `itemid` | 1 | uint64 | optional |  |
| `matchid` | 2 | uint64 | optional |  |
| `eventid` | 3 | int32 | optional |  |

### `CMsgGCCStrike15_v2_ClientAccountBalance`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `amount` | 1 | uint64 | optional |  |
| `url` | 2 | string | optional |  |

### `CMsgGCCStrike15_v2_ClientPartyJoinRelay`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `accountid` | 1 | uint32 | optional |  |
| `lobbyid` | 2 | uint64 | optional |  |

### `CMsgGCCStrike15_v2_ClientPartyWarning`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `entries` | 1 | CMsgGCCStrike15_v2_ClientPartyWarning.Entry | repeated |  |

### `CMsgGCCStrike15_v2_SetEventFavorite`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `eventid` | 1 | uint64 | optional |  |
| `is_favorite` | 2 | bool | optional |  |

### `CMsgGCCStrike15_v2_GetEventFavorites_Request`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `all_events` | 1 | bool | optional |  |

### `CMsgGCCStrike15_v2_GetEventFavorites_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `all_events` | 1 | bool | optional |  |
| `json_favorites` | 2 | string | optional |  |
| `json_featured` | 3 | string | optional |  |

### `CMsgGCCStrike15_v2_ClientPerfReport`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `entries` | 1 | CMsgGCCStrike15_v2_ClientPerfReport.Entry | repeated |  |

### `CVDiagnostic`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `id` | 1 | uint32 | optional |  |
| `extended` | 2 | uint32 | optional |  |
| `value` | 3 | uint64 | optional |  |
| `string_value` | 4 | string | optional |  |

### `CMsgGCCStrike15_v2_GC2ClientRefuseSecureMode`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `file_report` | 1 | string | optional |  |
| `offer_insecure_mode` | 2 | bool | optional |  |
| `offer_secure_mode` | 3 | bool | optional |  |
| `show_unsigned_ui` | 4 | bool | optional |  |
| `kick_user` | 5 | bool | optional |  |
| `show_trusted_ui` | 6 | bool | optional |  |
| `show_warning_not_trusted` | 7 | bool | optional |  |
| `show_warning_not_trusted_2` | 8 | bool | optional |  |
| `files_prevented_trusted` | 9 | string | optional |  |

### `CMsgGCCStrike15_v2_GC2ClientRequestValidation`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `full_report` | 1 | bool | optional |  |
| `module` | 2 | string | optional |  |

### `CMsgGCCStrike15_v2_GC2ClientInitSystem`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `load` | 1 | bool | optional |  |
| `name` | 2 | string | optional |  |
| `outputname` | 3 | string | optional |  |
| `key_data` | 4 | bytes | optional |  |
| `sha_hash` | 5 | bytes | optional |  |
| `cookie` | 6 | int32 | optional |  |
| `manifest` | 7 | string | optional |  |
| `system_package` | 8 | bytes | optional |  |
| `load_system` | 9 | bool | optional |  |

### `CMsgGCCStrike15_v2_GC2ClientInitSystem_Response`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `success` | 1 | bool | optional |  |
| `diagnostic` | 2 | string | optional |  |
| `sha_hash` | 3 | bytes | optional |  |
| `response` | 4 | int32 | optional |  |
| `error_code1` | 5 | int32 | optional |  |
| `error_code2` | 6 | int32 | optional |  |
| `handle` | 7 | int64 | optional |  |
| `einit_result` | 8 | [EInitSystemResult](#einitsystemresult) | optional | *(default: `k_EInitSystemResult_Invalid`)* |
| `aux_system1` | 9 | int32 | optional |  |
| `aux_system2` | 10 | int32 | optional |  |

### `CMsgGCCStrike15_v2_SetPlayerLeaderboardSafeName`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `leaderboard_safe_name` | 1 | string | optional |  |

### `CMsgRequestRecurringMissionSchedule`

### `CMsgRecurringMissionSchema`

| Field | Ordinal | Type | Label | Description |
|-------|---------|------|-------|-------------|
| `missions` | 1 | CMsgRecurringMissionSchema.MissionTemplateList | repeated |  |
