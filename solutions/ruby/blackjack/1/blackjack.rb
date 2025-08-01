# frozen_string_literal: true

# Blackjack exercise
module Blackjack
  CARDS = { two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, ten: 10, jack: 10, queen: 10,
            king: 10, ace: 11 }.freeze

  def self.parse_card(card) = CARDS[card.to_sym] || 0

  def self.card_range(card1, card2)
    case parse_card(card1) + parse_card(card2)
    when 4..11 then 'low'
    when 12..16 then 'mid'
    when 17..20 then 'high'
    when 21 then 'blackjack'
    end
  end

  def self.first_turn(card1, card2, dealer_card) # rubocop:disable Metrics/CyclomaticComplexity
    case card_range(card1, card2)
    when 'low' then 'H'
    when 'mid' then parse_card(dealer_card) >= 7 ? 'H' : 'S'
    when 'high' then 'S'
    when 'blackjack' then parse_card(dealer_card) >= 10 ? 'S' : 'W'
    else 'P' if card1 == 'ace' && card2 == 'ace'
    end
  end
end
