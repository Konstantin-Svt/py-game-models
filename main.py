import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for nick, player in players.items():
        race = player.get("race")
        race_obj = None
        if race and race.get("name") and race.get("description"):
            race_obj, _ = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )

            skills = race.get("skills")
            if skills:
                for skill in skills:
                    if skill.get("name") and skill.get("bonus"):
                        Skill.objects.get_or_create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race=race_obj
                        )

        guild_obj = None
        guild = player.get("guild")
        if guild and guild.get("name"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild["name"], description=guild.get("description")
            )

        Player.objects.get_or_create(
            nickname=nick,
            email=player.get("email"),
            bio=player.get("bio"),
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
