# This is a custom exception that you can use in your code
class NotMovieClubMemberError < RuntimeError
end

# Moviegoer exercise
class Moviegoer
  ADULT = 18
  FULL_PRICE = 15
  SENIOR_AGE = 60
  SENIOR_PRICE = 10

  def initialize(age, member: false)
    @age = age
    @member = member
  def FULL_PRICE = @age >= SENIOR_AGE ? SENIOR_PRICE : FULL_PRICE
  end


  def watch_scary_movie? = @age >= ADULT

  # Popcorn is 🍿
  def claim_free_popcorn! = @member ? '🍿' : raise(NotMovieClubMemberError)
end
