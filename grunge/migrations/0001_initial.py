# Generated by Django 3.1.1 on 2020-09-07 21:23

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                ("name", models.CharField(help_text="The album name", max_length=100)),
                (
                    "year",
                    models.PositiveSmallIntegerField(
                        help_text="The year the album was released"
                    ),
                ),
            ],
            options={
                "ordering": ("artist", "year", "name"),
            },
        ),
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                ("name", models.CharField(help_text="The artist name", max_length=100)),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Playlist",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="The playlist name", max_length=100),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Track",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="The track name", max_length=100),
                ),
                (
                    "number",
                    models.PositiveSmallIntegerField(
                        help_text="The track number on the album"
                    ),
                ),
                (
                    "album",
                    models.ForeignKey(
                        help_text="The album this track appears on",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tracks",
                        to="grunge.album",
                    ),
                ),
            ],
            options={
                "ordering": ("number", "name"),
            },
        ),
        migrations.CreateModel(
            name="PlaylistTrack",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                (
                    "number",
                    models.PositiveSmallIntegerField(
                        help_text="The track number on the playlist"
                    ),
                ),
                (
                    "playlist",
                    models.ForeignKey(
                        help_text="The playlist this track appears on",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="grunge.playlist",
                    ),
                ),
                (
                    "track",
                    models.ForeignKey(
                        help_text="The track on this playlist",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="grunge.track",
                    ),
                ),
            ],
            options={
                "ordering": ("number",),
            },
        ),
        migrations.AddField(
            model_name="playlist",
            name="tracks",
            field=models.ManyToManyField(
                help_text="The tracks on the playlist",
                related_name="playlists",
                through="grunge.PlaylistTrack",
                to="grunge.Track",
            ),
        ),
        migrations.AddIndex(
            model_name="artist",
            index=models.Index(fields=["name"], name="grunge_arti_name_b98e4f_idx"),
        ),
        migrations.AddField(
            model_name="album",
            name="artist",
            field=models.ForeignKey(
                help_text="The artist that produced the album",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="albums",
                to="grunge.artist",
            ),
        ),
        migrations.AddIndex(
            model_name="track",
            index=models.Index(
                fields=["number", "name"], name="grunge_trac_number_40d766_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="track",
            constraint=models.UniqueConstraint(
                fields=("album", "number"), name="unique_album_number"
            ),
        ),
        migrations.AddConstraint(
            model_name="playlisttrack",
            constraint=models.UniqueConstraint(
                fields=("playlist", "track", "number"),
                name="unique_playlist_track_number",
            ),
        ),
        migrations.AddIndex(
            model_name="album",
            index=models.Index(
                fields=["artist", "year", "name"], name="grunge_albu_artist__78041d_idx"
            ),
        ),
    ]
