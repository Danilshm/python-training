def main():
    health= 5 
    armor = 5
    add_armor(health,armor)
def add_armor(a,b):
    new_health= a +b
    print_health(new_health)
def print_health(new_health):
    print(f"the player now has {new_health} health")
main()
def to_celcius(f):
    celcius = 5/9 * (f-32)
    return celcius
def test(f):
    c = round(to_celcius(f),2)
    print(f, "degrees farenheit is", c, "degree celsium")
test(100)
test(88)
def hours_to_seconds(hours):
    seconds=hours*60*60
    return seconds 
def test1(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")
test1(10)
test1(1)
def days_and_hours_went(days,hours):
    went=days*24+hours
    return(went)
print(days_and_hours_went(9,6), " times went")
def total_xp(level, xp_to_add):
    base_xp = level*100 + xp_to_add
    return base_xp
print(total_xp(1,100))
def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power*amp
    damage_dealth = total_damage - resist 
    new_health = health - damage_dealth
    return new_health 
print(take_magic_damage(100,5 ,2 ,20))
def unlock_achievement(before_xp, ach_xp, ach_name): 
    sum_xp = before_xp + ach_xp
    alert= f"Achievement Unlocked: {ach_name}"
    return sum_xp, alert
print(unlock_achievement(20,30,"Banana"))
def update_player_score(current_score, increment): 
    current_score = current_score+increment
    return current_score
def get_hurt(current_health, damage):
    current_health-=damage 
    return current_health
print(get_hurt(200, 10))
print(get_hurt(100,25))
print("Start")
can_create = 0b1000
can_review = 0b0100
can_delete = 0b0010
can_edit = 0b0001
def get_create_bits(user_permissions):
    return user_permissions & can_create
def get_review_bits(user_permissions):
    return user_permissions & can_review
def get_delete_bits(user_permissions):
    return user_permissions & can_delete
def get_edit_bits(user_permissions):
    return user_permissions & can_edit
if (get_create_bits(0b0110)) != 0:
    print("True")
else:
    print("False")
create_bits = get_create_bits(0b0110)
print(bin(create_bits))
review_bits = get_review_bits(0b0110)
print(bin(review_bits))
print(bin(get_delete_bits(0b0110)))
print(bin(get_edit_bits(0b0110)))
def calculate_guild_perms(glor,galad,elen,elr):
    party_permissions = glor | galad | elen | elr
    return party_permissions
print(bin(calculate_guild_perms(0b0001, 0b0011, 0b1100, 0b1000)))
print("player 1 and player 2")
def player_1_wins(player_1_score,player_2_score):
    return player_1_score>player_2_score
print(player_1_wins(10,5))
def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor>=enemy_damage
print(can_withstand_blow(5,2))
print(can_withstand_blow(5,5))
def print_status(player_health_):
    if player_health_ == 0:
        print("dead")
    print("status check complete")
print_status(3)
print_status(0)
def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords==number_of_soldiers:
        return "correct amount"
    else: 
        return "incorrect amount"
def player_status(health):
    if health <=0:
        return "dead"
    elif health<=5:
        return "injured"
    else:
        return "healthy"
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name== high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"
banan = check_high_score(12,19)
print(banan)
def does_attack_hit(attack_roll, armor_class):
    if (attack_roll != 1) & (attack_roll>= armor_class) | (attack_roll==20):
        return True
    else: 
        return False 
does_attack_hit_number= does_attack_hit(6,5)
print(does_attack_hit_number)
def should_serve_customer(customer_age, on_break, time):
    condition_1 = customer_age>= 21
    condition_3 = 5< time < 10
    return condition_1 and not on_break and condition_3
print(should_serve_customer(21,False,6))
def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)
def sum_of_numbers(start,end):
    total = 0
    for i in range(start,end):
        total += i 
    return total
print(sum_of_numbers(0,5))
player_iventory= [200, "Iron", "Gold"]
print(f"Inventory: {player_iventory}")