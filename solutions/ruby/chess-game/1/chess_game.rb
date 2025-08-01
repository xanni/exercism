# Chess exercise
module Chess
  RANKS = 1..8
  FILES = 'A'..'H'
  INVALID_MSG = ' attempted to move to %s, but that is not a valid square'.freeze
  VALID_MSG = ' moved to %s'.freeze

  def self.valid_square?(rank, file) = RANKS.include?(rank) && FILES.include?(file)

  def self.nick_name(first_name, last_name) = (first_name[0, 2] + last_name[-2, 2]).upcase

  def self.move_message(first_name, last_name, square) = nick_name(first_name, last_name) +
    ((valid_square?(Integer(square[1]), square[0]) ? VALID_MSG : INVALID_MSG) % square)
end
