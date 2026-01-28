package LanguageList;

use 5.038;

our @Languages;

sub add_language ($language) {
    return push @Languages, $language;
}

sub remove_language () {
    return pop @Languages;
}

sub first_language () {
    return $Languages[0];
}

sub last_language () {
    return $Languages[-1];
}

sub get_languages (@elements) {
    return @Languages[ map { $_ - 1 } @elements ];    # @elements are 1-based
}

sub has_language ($language) {
    return grep { $_ eq $language } @Languages;
}

1;
