PGDMP     9    *                w           jez_database    9.6.14    9.6.14 �    ,	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            -	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            .	           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            /	           1262    25340    jez_database    DATABASE     �   CREATE DATABASE jez_database WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United Kingdom.1252' LC_CTYPE = 'English_United Kingdom.1252';
    DROP DATABASE jez_database;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            0	           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12387    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            1	           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    25489    account_student    TABLE     �   CREATE TABLE public.account_student (
    id integer NOT NULL,
    email_ver boolean NOT NULL,
    studij_id_id character varying(10) NOT NULL,
    user_id integer NOT NULL,
    profile_image character varying(100) NOT NULL
);
 #   DROP TABLE public.account_student;
       public         postgres    false    3            �            1259    25487    account_student_id_seq    SEQUENCE        CREATE SEQUENCE public.account_student_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.account_student_id_seq;
       public       postgres    false    3    205            2	           0    0    account_student_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.account_student_id_seq OWNED BY public.account_student.id;
            public       postgres    false    204            �            1259    25499    account_student_kolegij    TABLE     }   CREATE TABLE public.account_student_kolegij (
    id integer NOT NULL,
    kolegij_id_id integer,
    username_id integer
);
 +   DROP TABLE public.account_student_kolegij;
       public         postgres    false    3            �            1259    25497    account_student_kolegij_id_seq    SEQUENCE     �   CREATE SEQUENCE public.account_student_kolegij_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.account_student_kolegij_id_seq;
       public       postgres    false    3    207            3	           0    0    account_student_kolegij_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.account_student_kolegij_id_seq OWNED BY public.account_student_kolegij.id;
            public       postgres    false    206            �            1259    25393 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         postgres    false    3            �            1259    25391    auth_group_id_seq    SEQUENCE     z   CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       postgres    false    195    3            4	           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
            public       postgres    false    194            �            1259    25403    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         postgres    false    3            �            1259    25401    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       postgres    false    197    3            5	           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
            public       postgres    false    196            �            1259    25385    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         postgres    false    3            �            1259    25383    auth_permission_id_seq    SEQUENCE        CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       postgres    false    3    193            6	           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
            public       postgres    false    192            �            1259    25411 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         postgres    false    3            �            1259    25421    auth_user_groups    TABLE        CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         postgres    false    3            �            1259    25419    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public       postgres    false    201    3            7	           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
            public       postgres    false    200            �            1259    25409    auth_user_id_seq    SEQUENCE     y   CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public       postgres    false    199    3            8	           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
            public       postgres    false    198            �            1259    25429    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         postgres    false    3            �            1259    25427 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public       postgres    false    3    203            9	           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
            public       postgres    false    202            �            1259    25531    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         postgres    false    3            �            1259    25529    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       postgres    false    3    209            :	           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
            public       postgres    false    208            �            1259    25375    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         postgres    false    3            �            1259    25373    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       postgres    false    191    3            ;	           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
            public       postgres    false    190            �            1259    25343    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         postgres    false    3            �            1259    25341    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public       postgres    false    186    3            <	           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
            public       postgres    false    185            �            1259    25611    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         postgres    false    3            �            1259    25575    objava_editobjave    TABLE     �   CREATE TABLE public.objava_editobjave (
    edit_objave_id integer NOT NULL,
    date timestamp with time zone NOT NULL,
    objava_id_id integer NOT NULL,
    tekst_id integer NOT NULL,
    username_id integer NOT NULL
);
 %   DROP TABLE public.objava_editobjave;
       public         postgres    false    3            �            1259    25573 $   objava_editobjave_edit_objave_id_seq    SEQUENCE     �   CREATE SEQUENCE public.objava_editobjave_edit_objave_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.objava_editobjave_edit_objave_id_seq;
       public       postgres    false    3    213            =	           0    0 $   objava_editobjave_edit_objave_id_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.objava_editobjave_edit_objave_id_seq OWNED BY public.objava_editobjave.edit_objave_id;
            public       postgres    false    212            �            1259    25564    objava_objava    TABLE       CREATE TABLE public.objava_objava (
    objava_id integer NOT NULL,
    date timestamp with time zone NOT NULL,
    likes integer NOT NULL,
    allow_edit boolean NOT NULL,
    tekst text NOT NULL,
    kolegij_id_id integer NOT NULL,
    username_id integer NOT NULL
);
 !   DROP TABLE public.objava_objava;
       public         postgres    false    3            �            1259    25562    objava_objava_objava_id_seq    SEQUENCE     �   CREATE SEQUENCE public.objava_objava_objava_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.objava_objava_objava_id_seq;
       public       postgres    false    211    3            >	           0    0    objava_objava_objava_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.objava_objava_objava_id_seq OWNED BY public.objava_objava.objava_id;
            public       postgres    false    210            �            1259    25359    studij_kolegij    TABLE     �   CREATE TABLE public.studij_kolegij (
    dummy_id integer NOT NULL,
    kolegij_id character varying(10) NOT NULL,
    kolegij_ime character varying(60) NOT NULL,
    semestar smallint NOT NULL,
    studij_id_id character varying(10) NOT NULL
);
 "   DROP TABLE public.studij_kolegij;
       public         postgres    false    3            �            1259    25357    studij_kolegij_dummy_id_seq    SEQUENCE     �   CREATE SEQUENCE public.studij_kolegij_dummy_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.studij_kolegij_dummy_id_seq;
       public       postgres    false    189    3            ?	           0    0    studij_kolegij_dummy_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.studij_kolegij_dummy_id_seq OWNED BY public.studij_kolegij.dummy_id;
            public       postgres    false    188            �            1259    25352    studij_studij    TABLE     �   CREATE TABLE public.studij_studij (
    studij_id character varying(10) NOT NULL,
    studij_ime character varying(60) NOT NULL
);
 !   DROP TABLE public.studij_studij;
       public         postgres    false    3            5           2604    25492    account_student id    DEFAULT     x   ALTER TABLE ONLY public.account_student ALTER COLUMN id SET DEFAULT nextval('public.account_student_id_seq'::regclass);
 A   ALTER TABLE public.account_student ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    205    204    205            6           2604    25502    account_student_kolegij id    DEFAULT     �   ALTER TABLE ONLY public.account_student_kolegij ALTER COLUMN id SET DEFAULT nextval('public.account_student_kolegij_id_seq'::regclass);
 I   ALTER TABLE public.account_student_kolegij ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    207    206    207            0           2604    25396    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    195    194    195            1           2604    25406    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    197    196    197            /           2604    25388    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    192    193    193            2           2604    25414    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    198    199    199            3           2604    25424    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    200    201    201            4           2604    25432    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    202    203    203            7           2604    25534    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    208    209    209            .           2604    25378    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    191    190    191            ,           2604    25346    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    186    185    186            :           2604    25578     objava_editobjave edit_objave_id    DEFAULT     �   ALTER TABLE ONLY public.objava_editobjave ALTER COLUMN edit_objave_id SET DEFAULT nextval('public.objava_editobjave_edit_objave_id_seq'::regclass);
 O   ALTER TABLE public.objava_editobjave ALTER COLUMN edit_objave_id DROP DEFAULT;
       public       postgres    false    213    212    213            9           2604    25567    objava_objava objava_id    DEFAULT     �   ALTER TABLE ONLY public.objava_objava ALTER COLUMN objava_id SET DEFAULT nextval('public.objava_objava_objava_id_seq'::regclass);
 F   ALTER TABLE public.objava_objava ALTER COLUMN objava_id DROP DEFAULT;
       public       postgres    false    210    211    211            -           2604    25362    studij_kolegij dummy_id    DEFAULT     �   ALTER TABLE ONLY public.studij_kolegij ALTER COLUMN dummy_id SET DEFAULT nextval('public.studij_kolegij_dummy_id_seq'::regclass);
 F   ALTER TABLE public.studij_kolegij ALTER COLUMN dummy_id DROP DEFAULT;
       public       postgres    false    189    188    189             	          0    25489    account_student 
   TABLE DATA               ^   COPY public.account_student (id, email_ver, studij_id_id, user_id, profile_image) FROM stdin;
    public       postgres    false    205   ��       @	           0    0    account_student_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.account_student_id_seq', 16, true);
            public       postgres    false    204            "	          0    25499    account_student_kolegij 
   TABLE DATA               Q   COPY public.account_student_kolegij (id, kolegij_id_id, username_id) FROM stdin;
    public       postgres    false    207   d�       A	           0    0    account_student_kolegij_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.account_student_kolegij_id_seq', 1, false);
            public       postgres    false    206            	          0    25393 
   auth_group 
   TABLE DATA               .   COPY public.auth_group (id, name) FROM stdin;
    public       postgres    false    195   ��       B	           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
            public       postgres    false    194            	          0    25403    auth_group_permissions 
   TABLE DATA               M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       postgres    false    197   ��       C	           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
            public       postgres    false    196            	          0    25385    auth_permission 
   TABLE DATA               N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       postgres    false    193   ��       D	           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 48, true);
            public       postgres    false    192            	          0    25411 	   auth_user 
   TABLE DATA               �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public       postgres    false    199   ��       	          0    25421    auth_user_groups 
   TABLE DATA               A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public       postgres    false    201   j�       E	           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
            public       postgres    false    200            F	           0    0    auth_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_user_id_seq', 18, true);
            public       postgres    false    198            	          0    25429    auth_user_user_permissions 
   TABLE DATA               P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       postgres    false    203   ��       G	           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
            public       postgres    false    202            $	          0    25531    django_admin_log 
   TABLE DATA               �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public       postgres    false    209   ��       H	           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 19, true);
            public       postgres    false    208            	          0    25375    django_content_type 
   TABLE DATA               C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public       postgres    false    191   C�       I	           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 12, true);
            public       postgres    false    190            	          0    25343    django_migrations 
   TABLE DATA               C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public       postgres    false    186   ��       J	           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 24, true);
            public       postgres    false    185            )	          0    25611    django_session 
   TABLE DATA               P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public       postgres    false    214   ��       (	          0    25575    objava_editobjave 
   TABLE DATA               f   COPY public.objava_editobjave (edit_objave_id, date, objava_id_id, tekst_id, username_id) FROM stdin;
    public       postgres    false    213   �       K	           0    0 $   objava_editobjave_edit_objave_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public.objava_editobjave_edit_objave_id_seq', 1, false);
            public       postgres    false    212            &	          0    25564    objava_objava 
   TABLE DATA               n   COPY public.objava_objava (objava_id, date, likes, allow_edit, tekst, kolegij_id_id, username_id) FROM stdin;
    public       postgres    false    211   *�       L	           0    0    objava_objava_objava_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.objava_objava_objava_id_seq', 1, false);
            public       postgres    false    210            	          0    25359    studij_kolegij 
   TABLE DATA               c   COPY public.studij_kolegij (dummy_id, kolegij_id, kolegij_ime, semestar, studij_id_id) FROM stdin;
    public       postgres    false    189   G�       M	           0    0    studij_kolegij_dummy_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.studij_kolegij_dummy_id_seq', 5, true);
            public       postgres    false    188            	          0    25352    studij_studij 
   TABLE DATA               >   COPY public.studij_studij (studij_id, studij_ime) FROM stdin;
    public       postgres    false    187   ��       q           2606    25504 4   account_student_kolegij account_student_kolegij_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.account_student_kolegij
    ADD CONSTRAINT account_student_kolegij_pkey PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public.account_student_kolegij DROP CONSTRAINT account_student_kolegij_pkey;
       public         postgres    false    207    207            j           2606    25494 $   account_student account_student_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.account_student
    ADD CONSTRAINT account_student_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.account_student DROP CONSTRAINT account_student_pkey;
       public         postgres    false    205    205            n           2606    25496 +   account_student account_student_user_id_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.account_student
    ADD CONSTRAINT account_student_user_id_key UNIQUE (user_id);
 U   ALTER TABLE ONLY public.account_student DROP CONSTRAINT account_student_user_id_key;
       public         postgres    false    205    205            O           2606    25560    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         postgres    false    195    195            T           2606    25455 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public         postgres    false    197    197    197            W           2606    25408 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         postgres    false    197    197            Q           2606    25398    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         postgres    false    195    195            J           2606    25441 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public         postgres    false    193    193    193            L           2606    25390 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         postgres    false    193    193            _           2606    25426 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public         postgres    false    201    201            b           2606    25470 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public         postgres    false    201    201    201            Y           2606    25416    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public         postgres    false    199    199            e           2606    25434 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public         postgres    false    203    203            h           2606    25484 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public         postgres    false    203    203    203            \           2606    25554     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public         postgres    false    199    199            u           2606    25540 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         postgres    false    209    209            E           2606    25382 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public         postgres    false    191    191    191            G           2606    25380 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         postgres    false    191    191            <           2606    25351 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public         postgres    false    186    186            �           2606    25618 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         postgres    false    214    214            }           2606    25580 (   objava_editobjave objava_editobjave_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.objava_editobjave
    ADD CONSTRAINT objava_editobjave_pkey PRIMARY KEY (edit_objave_id);
 R   ALTER TABLE ONLY public.objava_editobjave DROP CONSTRAINT objava_editobjave_pkey;
       public         postgres    false    213    213            y           2606    25572     objava_objava objava_objava_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.objava_objava
    ADD CONSTRAINT objava_objava_pkey PRIMARY KEY (objava_id);
 J   ALTER TABLE ONLY public.objava_objava DROP CONSTRAINT objava_objava_pkey;
       public         postgres    false    211    211            A           2606    25364 "   studij_kolegij studij_kolegij_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.studij_kolegij
    ADD CONSTRAINT studij_kolegij_pkey PRIMARY KEY (dummy_id);
 L   ALTER TABLE ONLY public.studij_kolegij DROP CONSTRAINT studij_kolegij_pkey;
       public         postgres    false    189    189            >           2606    25356     studij_studij studij_studij_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.studij_studij
    ADD CONSTRAINT studij_studij_pkey PRIMARY KEY (studij_id);
 J   ALTER TABLE ONLY public.studij_studij DROP CONSTRAINT studij_studij_pkey;
       public         postgres    false    187    187            o           1259    25527 .   account_student_kolegij_kolegij_id_id_4fbaf50b    INDEX     {   CREATE INDEX account_student_kolegij_kolegij_id_id_4fbaf50b ON public.account_student_kolegij USING btree (kolegij_id_id);
 B   DROP INDEX public.account_student_kolegij_kolegij_id_id_4fbaf50b;
       public         postgres    false    207            r           1259    25528 ,   account_student_kolegij_username_id_683259b4    INDEX     w   CREATE INDEX account_student_kolegij_username_id_683259b4 ON public.account_student_kolegij USING btree (username_id);
 @   DROP INDEX public.account_student_kolegij_username_id_683259b4;
       public         postgres    false    207            k           1259    25515 %   account_student_studij_id_id_657d0aa4    INDEX     i   CREATE INDEX account_student_studij_id_id_657d0aa4 ON public.account_student USING btree (studij_id_id);
 9   DROP INDEX public.account_student_studij_id_id_657d0aa4;
       public         postgres    false    205            l           1259    25516 *   account_student_studij_id_id_657d0aa4_like    INDEX     �   CREATE INDEX account_student_studij_id_id_657d0aa4_like ON public.account_student USING btree (studij_id_id varchar_pattern_ops);
 >   DROP INDEX public.account_student_studij_id_id_657d0aa4_like;
       public         postgres    false    205            M           1259    25561    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public         postgres    false    195            R           1259    25456 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public         postgres    false    197            U           1259    25457 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public         postgres    false    197            H           1259    25442 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public         postgres    false    193            ]           1259    25472 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public         postgres    false    201            `           1259    25471 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public         postgres    false    201            c           1259    25486 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public         postgres    false    203            f           1259    25485 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public         postgres    false    203            Z           1259    25555     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public         postgres    false    199            s           1259    25551 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public         postgres    false    209            v           1259    25552 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public         postgres    false    209            �           1259    25620 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public         postgres    false    214            �           1259    25619 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public         postgres    false    214            {           1259    25608 '   objava_editobjave_objava_id_id_27546f95    INDEX     m   CREATE INDEX objava_editobjave_objava_id_id_27546f95 ON public.objava_editobjave USING btree (objava_id_id);
 ;   DROP INDEX public.objava_editobjave_objava_id_id_27546f95;
       public         postgres    false    213            ~           1259    25609 #   objava_editobjave_tekst_id_2d124e6d    INDEX     e   CREATE INDEX objava_editobjave_tekst_id_2d124e6d ON public.objava_editobjave USING btree (tekst_id);
 7   DROP INDEX public.objava_editobjave_tekst_id_2d124e6d;
       public         postgres    false    213                       1259    25610 &   objava_editobjave_username_id_9aa152ab    INDEX     k   CREATE INDEX objava_editobjave_username_id_9aa152ab ON public.objava_editobjave USING btree (username_id);
 :   DROP INDEX public.objava_editobjave_username_id_9aa152ab;
       public         postgres    false    213            w           1259    25591 $   objava_objava_kolegij_id_id_d4d05d98    INDEX     g   CREATE INDEX objava_objava_kolegij_id_id_d4d05d98 ON public.objava_objava USING btree (kolegij_id_id);
 8   DROP INDEX public.objava_objava_kolegij_id_id_d4d05d98;
       public         postgres    false    211            z           1259    25592 "   objava_objava_username_id_2f32b5fb    INDEX     c   CREATE INDEX objava_objava_username_id_2f32b5fb ON public.objava_objava USING btree (username_id);
 6   DROP INDEX public.objava_objava_username_id_2f32b5fb;
       public         postgres    false    211            B           1259    25371 $   studij_kolegij_studij_id_id_3f7b48fb    INDEX     g   CREATE INDEX studij_kolegij_studij_id_id_3f7b48fb ON public.studij_kolegij USING btree (studij_id_id);
 8   DROP INDEX public.studij_kolegij_studij_id_id_3f7b48fb;
       public         postgres    false    189            C           1259    25372 )   studij_kolegij_studij_id_id_3f7b48fb_like    INDEX     �   CREATE INDEX studij_kolegij_studij_id_id_3f7b48fb_like ON public.studij_kolegij USING btree (studij_id_id varchar_pattern_ops);
 =   DROP INDEX public.studij_kolegij_studij_id_id_3f7b48fb_like;
       public         postgres    false    189            ?           1259    25365 %   studij_studij_studij_id_9f199f46_like    INDEX     x   CREATE INDEX studij_studij_studij_id_9f199f46_like ON public.studij_studij USING btree (studij_id varchar_pattern_ops);
 9   DROP INDEX public.studij_studij_studij_id_9f199f46_like;
       public         postgres    false    187            �           2606    25517 P   account_student_kolegij account_student_kole_kolegij_id_id_4fbaf50b_fk_studij_ko    FK CONSTRAINT     �   ALTER TABLE ONLY public.account_student_kolegij
    ADD CONSTRAINT account_student_kole_kolegij_id_id_4fbaf50b_fk_studij_ko FOREIGN KEY (kolegij_id_id) REFERENCES public.studij_kolegij(dummy_id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.account_student_kolegij DROP CONSTRAINT account_student_kole_kolegij_id_id_4fbaf50b_fk_studij_ko;
       public       postgres    false    2113    207    189            �           2606    25522 N   account_student_kolegij account_student_kole_username_id_683259b4_fk_account_s    FK CONSTRAINT     �   ALTER TABLE ONLY public.account_student_kolegij
    ADD CONSTRAINT account_student_kole_username_id_683259b4_fk_account_s FOREIGN KEY (username_id) REFERENCES public.account_student(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.account_student_kolegij DROP CONSTRAINT account_student_kole_username_id_683259b4_fk_account_s;
       public       postgres    false    205    207    2154            �           2606    25505 B   account_student account_student_studij_id_id_657d0aa4_fk_studij_st    FK CONSTRAINT     �   ALTER TABLE ONLY public.account_student
    ADD CONSTRAINT account_student_studij_id_id_657d0aa4_fk_studij_st FOREIGN KEY (studij_id_id) REFERENCES public.studij_studij(studij_id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.account_student DROP CONSTRAINT account_student_studij_id_id_657d0aa4_fk_studij_st;
       public       postgres    false    205    2110    187            �           2606    25510 @   account_student account_student_user_id_cbbf6595_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.account_student
    ADD CONSTRAINT account_student_user_id_cbbf6595_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 j   ALTER TABLE ONLY public.account_student DROP CONSTRAINT account_student_user_id_cbbf6595_fk_auth_user_id;
       public       postgres    false    199    205    2137            �           2606    25449 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public       postgres    false    193    197    2124            �           2606    25444 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public       postgres    false    195    197    2129            �           2606    25435 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public       postgres    false    2119    193    191            �           2606    25464 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public       postgres    false    2129    201    195            �           2606    25459 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public       postgres    false    201    199    2137            �           2606    25478 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public       postgres    false    2124    203    193            �           2606    25473 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public       postgres    false    203    199    2137            �           2606    25541 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public       postgres    false    191    2119    209            �           2606    25546 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public       postgres    false    199    209    2137            �           2606    25593 F   objava_editobjave objava_editobjave_objava_id_id_27546f95_fk_objava_ob    FK CONSTRAINT     �   ALTER TABLE ONLY public.objava_editobjave
    ADD CONSTRAINT objava_editobjave_objava_id_id_27546f95_fk_objava_ob FOREIGN KEY (objava_id_id) REFERENCES public.objava_objava(objava_id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.objava_editobjave DROP CONSTRAINT objava_editobjave_objava_id_id_27546f95_fk_objava_ob;
       public       postgres    false    211    2169    213            �           2606    25598 P   objava_editobjave objava_editobjave_tekst_id_2d124e6d_fk_objava_objava_objava_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.objava_editobjave
    ADD CONSTRAINT objava_editobjave_tekst_id_2d124e6d_fk_objava_objava_objava_id FOREIGN KEY (tekst_id) REFERENCES public.objava_objava(objava_id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.objava_editobjave DROP CONSTRAINT objava_editobjave_tekst_id_2d124e6d_fk_objava_objava_objava_id;
       public       postgres    false    211    2169    213            �           2606    25603 N   objava_editobjave objava_editobjave_username_id_9aa152ab_fk_account_student_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.objava_editobjave
    ADD CONSTRAINT objava_editobjave_username_id_9aa152ab_fk_account_student_id FOREIGN KEY (username_id) REFERENCES public.account_student(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.objava_editobjave DROP CONSTRAINT objava_editobjave_username_id_9aa152ab_fk_account_student_id;
       public       postgres    false    2154    213    205            �           2606    25581 M   objava_objava objava_objava_kolegij_id_id_d4d05d98_fk_studij_kolegij_dummy_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.objava_objava
    ADD CONSTRAINT objava_objava_kolegij_id_id_d4d05d98_fk_studij_kolegij_dummy_id FOREIGN KEY (kolegij_id_id) REFERENCES public.studij_kolegij(dummy_id) DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.objava_objava DROP CONSTRAINT objava_objava_kolegij_id_id_d4d05d98_fk_studij_kolegij_dummy_id;
       public       postgres    false    211    2113    189            �           2606    25586 F   objava_objava objava_objava_username_id_2f32b5fb_fk_account_student_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.objava_objava
    ADD CONSTRAINT objava_objava_username_id_2f32b5fb_fk_account_student_id FOREIGN KEY (username_id) REFERENCES public.account_student(id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.objava_objava DROP CONSTRAINT objava_objava_username_id_2f32b5fb_fk_account_student_id;
       public       postgres    false    211    205    2154            �           2606    25366 N   studij_kolegij studij_kolegij_studij_id_id_3f7b48fb_fk_studij_studij_studij_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.studij_kolegij
    ADD CONSTRAINT studij_kolegij_studij_id_id_3f7b48fb_fk_studij_studij_studij_id FOREIGN KEY (studij_id_id) REFERENCES public.studij_studij(studij_id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.studij_kolegij DROP CONSTRAINT studij_kolegij_studij_id_id_3f7b48fb_fk_studij_studij_studij_id;
       public       postgres    false    189    187    2110             	   �   x�m�]
�0���hWo�CD�D�֟��R�<�>,|���.(��t	�j���+��ڃ^]��Z.�q��H��1.i]�e���~l����;d󳣤���t!���5/��~?��A������[F��+I      "	      x������ � �      	      x������ � �      	      x������ � �      	   �  x�m�Kn�0��}
NPżֽF�����������cό�]l�?���ގY�u�m�3;n�S�����:r�j��
� ;{���~�`	�1�_���*��v��u�F�CM��	�u�y������F�X�/�}V�gm<.�cÛ�$9� �\Ă�jUB���M���U�ރ�� 7����q���Ǹ�e��[˶�lU8�f�9�c���J<�q�(3ѐ+��ի��j�8ҹ8�d�32qډa^d���H褯۽�C������!'��X(
�mB�(�&-:g�����U�x�guqx������y�̟���\��%�S�m�B����.n�L_w�J{�J�j$&9@7'4��%����D'n
sX\�nS݌���>Ze�?��R\"����0((v-�@Nt+l7l^Ye�?���3��#��ƹ�%	�H��mI0�2���E�xS      	   �  x���ۮ�����O�ܙF�I'�Y�x�t�*�Py�~��.{��.�s�Z������	���1F��Zb�{��r� 9@�pt7C��f4��fg��TU�[t~��&ȿ��.\'��|i�Nrʎ��[�qͩ��Y �{�ZV����@ <�1ź ��s�r2ozY�)S��wgsۚfN����k۷4X�z�����n�3H{I�C���jE�Ǒ���者N�)}B�� ��dR���t���Gh�,��ŵ�-��꞊0�ݟ-ջᄇ����q�k�d���o�!

�<��ʘmǀ�2���,Ԍܶ��o�?֬K/_�c&,�e$B*t��33��wל�k�oo�jX4��yO����bf�)1w(z�Xm1����������z��1�܀���Op�X�"�d@Z����l
2_K{���^$R|t��6�E��~�u���}�uШ�`���Ӆ�q�~���
ߖ���� �(��L��!
��r�or]���.%kܼ適�7�(ji�����h���{��E��l(pm̲��ɮE����2HYO)�����{�j~�ycS__��	}��	
�X�����ӽ���~Z�� ��W����Z���������~�� /H2����lZ��'��zᬡ���t�2b"Ff6v��1׎�^�N������&���C�	/a	Q���s�l:+�������r���n�[|\vBY̒f1���~�V7�M=sg~G���mg���ׄP!�'P�1� <'�f�X�!��\�\�ii��I �׼/u��MDM�������B���7�|�őW�����_��L=� ��N�ۆ7��p�Μl�=7��k[�x ��jpRT�p㈓^<X��tn�ǕrU�~�'8̮M�����ζ%D��s.4�������K�*[����X�f�|�6�M{m��8�ʪ:>_�a�v��w�^�k<��p�
���Uk���mɫL#<����ݳ���z~;�[��M�z���H� I�X$^���n"���0Q��/U���tD�t/,�do�c
��^<崍К�hj�,Q�� 2H>GQ��,���'�Ӂ�Յ�[��V.��~A<�ų������*���B�1�/L��PS��bw���j<�׍��4T|����� =Oz2�{����Va��'���S�.{�Uh��?.��/�������V2T5|�r䌷�	]襣\(��,��Z=��ϋ���yְG���"�U�X�C���a],v��˯\�)_]��n;_�S綺i�{�k��v�[{좕��K&�Y�O��а�˼���C�99��0�T�$~k��W��"�����u{����Q�K©�ڹ��F���K�����4(U<�qWZ��3���OhD!�h�b��|��r4��Aժ�>���������      	      x������ � �      	      x������ � �      $	   �  x����N1E��hՖ`��~�� �JTA�t7�d��S-Ѧ�2��=��	�K�K�-RF�>
H� Gn��Z$v�^������ۗ��'7T4���A' ~�#�� 1�eQ/)Z3@ܾ}h5T�G���(�4�餧I��=�/��n�w�q|^5?��S�e��xz�v��a�����)�&
SHK���=*�P�q�{R���%�3Dod՝
�Jx�L^�l��;�#KetiE��(�ˇ\�O����|V]�o��RՔ
�j4+�`��X��3��>�O<�-3=������2�y���۹T䳻�r͂ޢ�,�q܇�x�5]�3c��o-����ii0r
v`�(⪂@����O���3�׈��V���^cZ�g{7�j��~���e�F�      	   �   x�]��
�0D�w>�4��/���bc5+�M�����ҧ9s�q�!D��hiBE>ۋFNCPqXM�$�8�%+'���h�ͦ����L��[�B��%G#���C\���-=���m1��n_DY8G����oW�M���/�Ml      	     x����n�0���S�~Ud��y��,/qSW�Yc����v(!*-]	!$���瀫1N'�V!��v��δ ���|F�	�1=�k@���� U��h�������$+Ie������ Vi?�qO5��R�E�2�����8�*K�]���]��`;�:��9�6
�tsf�;��I�M���Kkκy��I�m� 0��%?y��:���tvE��b�ZLm�h�l��8搲^w�]��?���Ga���̚����q�.�BY��Cט�*�!~a�J,�F�f��{�R����+�譓�!y������o1^g�� t��9��i��D�R~����h�_U^a��-4��ͷ.���X|!�O�'J|�0�Q���gF8�M.��!9d���uՑ[�<0T�����ٛnRb�A�X��ߕ1,9*{�z��Ϋ2O^��ŵV�.��!�D1����R X��U�H��ǂ�M� ����C z�?V�ɞ ��L�F�]��C��1�ʬ����?i��      )	      x������ � �      (	      x������ � �      &	      x������ � �      	   x   x�3��u1��M,I�M,��NT0�4�,(..�2�%U�e�����Z���P�����Z�W���Y��]
�n������隓�]R����i�1��w7�(�O/J��,J��J5����qqq H�,�      	   x   x�+(..�(JM�,���-��T(.K-=қ��yta�WR����P�x��4/����,���������⒢�,���=.$X����d��J%�Q�9��@m%�y�٩ kR	Y��%F��� c6�     